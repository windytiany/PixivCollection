<template>
  <div
    :class="{
      dark: colorScheme === 'dark',
    }"
  >
    <div class="min-h-screen transition-colors dark:bg-[#1a1a1a] dark:text-white">
      <Sidebar />
      <SidebarMask />
      <Navbar />
      <MasonryView />
      <Tip v-if="loading">
        <IconLoading class="mx-auto w-[60px] pb-2" :dark="colorScheme === 'light'" />
        <div class="text-center">
          数据加载中<br>
          {{ formatBytes(receivedLength) }}<span v-if="contentLength"> / {{ formatBytes(contentLength) }}</span>
        </div>
      </Tip>
      <Tip v-if="!loading && !imagesFiltered.length">
        无数据
      </Tip>
      <ImageViewer />
      <ConfigDialog />
      <DebugInfo v-if="debug.enable" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { SettingType } from '@orilight/vue-settings'
import { useStore } from '@/store'
import { formatBytes, syncSettings } from '@/utils'
import { ONLINE_MODE, SERVER_ADDRESS } from '@/config'

const store = useStore()

const {
  loading,
  preferColorScheme,
  colorScheme,
  imagesFiltered,
  masonryConfig,
  filterConfig,
  debug,
} = toRefs(store)

const receivedLength = ref(0)
const contentLength = ref(0)

function regSettings() {
  store.settings.register('preferColorScheme', preferColorScheme)
  store.settings.register('masonryConfig', masonryConfig, SettingType.Json, {
    deepMerge: true,
  })
  store.settings.register('restrictConfig', toRef(filterConfig.value, 'restrict'), SettingType.Json, {
    deepMerge: true,
  })
}

async function fetchData() {
  try {
    const data = await fetch(`${SERVER_ADDRESS}/metadata`)
    const images = await data.json()
    store.images = images
    store.sortImages()
  }
  catch (error) {
    console.error('Error parsing response:', error)
  }
  finally {
    loading.value = false
  }
}

onMounted(() => {
  regSettings()
  if (ONLINE_MODE) {
    store.fetchFromAPI()
  }
  else {
    syncSettings()
      .then(_ => fetchData())
  }
})

onUnmounted(() => {
  store.settings.unregisterAll()
})
</script>

<style>
body {
  overflow-y: scroll;
}
</style>
