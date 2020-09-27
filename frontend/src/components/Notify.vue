<template>
    <div v-if="error" class="error_bar">
      <p>{{ error }}</p>
    </div>
</template>

<script>
export default {
    name: "Notify",
    props: {
        notify: String,
        error: Boolean
    },
}
</script>
