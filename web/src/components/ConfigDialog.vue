<template>
  <div v-show="showConfigDialog" class="fixed inset-0 flex items-center justify-center bg-black/50 p-4">
    <div class="w-full max-w-md rounded-lg bg-white p-6 shadow-xl dark:bg-gray-800">
      <div class="mb-6 flex items-center justify-between">
        <h2 class="text-xl font-semibold text-gray-800 dark:text-white">
          Settings
        </h2>
        <button
          class="text-gray-500 hover:text-gray-700 dark:text-gray-300 dark:hover:text-gray-100"
          @click="showConfigDialog = false"
        >
          ✕
        </button>
      </div>

      <div class="flex flex-col gap-4">
        <div class="mb-4 flex items-center gap-4">
          <label for="imagesPath" class="text-base">Images path</label>
          <input
            id="imagesPath"
            v-model="imagesPath"
            type="text"
            class="flex-1 rounded border border-gray-300 px-3 py-2 dark:border-gray-600 dark:bg-gray-700 dark:text-white"
            autocomplete="off"
          >
        </div>

        <div class="mb-8 flex items-center gap-4">
          <label for="jsonPath" class="text-base">Json Path</label>
          <input
            id="jsonPath"
            v-model="jsonPath"
            type="text"
            class="flex-1 rounded border border-gray-300 px-3 py-2 dark:border-gray-600 dark:bg-gray-700 dark:text-white"
            autocomplete="off"
          >
        </div>

        <div class="flex justify-end gap-2">
          <button
            type="button"
            class="rounded px-4 py-2 text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-700"
            @click="showConfigDialog = false"
          >
            Cancel
          </button>
          <button
            type="button"
            class="rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
            @click="saveConfig"
          >
            Save
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useStore } from '@/store'

const store = useStore()
const {
  showConfigDialog,
} = toRefs(store)

const config = localStorage.getItem('imagesConfig')
const configDict = config ? JSON.parse(config) : {}
const imagesPath = ref(configDict.imagesPath ? configDict.imagesPath : './image')
const jsonPath = ref(configDict.jsonPath ? configDict.jsonPath : './images.json')

function saveConfig() {
  configDict.imagesPath = imagesPath.value.replace(/\\/g, '/')
  configDict.jsonPath = jsonPath.value.replace(/\\/g, '/')
  localStorage.setItem('imagesConfig', JSON.stringify(configDict))
  showConfigDialog.value = false
  window.location.reload()
}
</script>
