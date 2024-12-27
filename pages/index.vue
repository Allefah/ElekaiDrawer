<script setup lang="ts">
import { Vue3JsonEditor } from "vue3-json-editor";
import { ref } from "vue";

const draw = async () => {
  const drawing = await $fetch("api/draw", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(json.value),
  });
  console.log(drawing);
  if (drawing.error) {
    data.value = drawing.error;
    return;
  } else {
    data.value = drawing;
  }
};

const json = ref({});
const data = ref();

function onJsonChange(value) {
  json.value = value;
}
</script>

<template>
  <div class="flex h-screen w-full bg-slate-900">
    <div class="w-1/2 h-screen p-2">
      <Vue3JsonEditor
        v-model="json"
        mode="text"
        @json-change="onJsonChange"
        class="h-screen"
      />
    </div>

    <div class="bg-slate-800">
      <button @click="draw()" class="p-2 bg-slate-600 text-blue-500">
        DRAW
      </button>
    </div>

    <div class="w-1/2 text-white" v-html="data"></div>
  </div>
</template>

<style>
.jsoneditor-vue {
  height: 100%;
  width: 100%;
}
.jsoneditor {
  border: none !important;
}
.jsoneditor-text {
  background-color: transparent !important;
  color: white !important;
  outline: black !important;
}
.jsoneditor-menu {
  background-color: transparent !important;
  border: none !important;
  outline: none !important;
}
.ace_editor,
.ace-jsoneditor {
  background-color: transparent;
}
</style>
