<template>
  <Header />
  <main class="container flex-grow px-4 mx-auto my-12">
    <slot />
  </main>
  <div>
  {{ groups }}
  </div>
  <Footer />
</template>

<script>
import Header from "./Header.vue"
import Footer from "./Footer.vue"

export default {
props: {
    posts: {
      type: Array,
      required: true,
    },
  },
  components: {
    Header,
    Footer,
  },
}
</script>
