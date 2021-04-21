<template>
  <Layout>
    <div id="app">
  		{{ groups }}
	</div>
  </Layout>
</template>

<script>
import Layout from "./components/Layout.vue"
import axios from "axios"

export default {
  components: {
    Layout,
  },
  data() {
    return {
      section: "home",
      groups: null,
    }
  },
  methods: {
  async fetchGroups() {
      try {
        this.error = null
        this.loading = true
        const url = `http://127.0.0.1:8000/group`
        const response = await axios.get(url)
        const results = response.data
        this.groups = results
        console.log(this.groups)
      } catch (err) {
        if (err.response) {
          // client received an error response (5xx, 4xx)
          this.error = {
            title: "Server Response",
            message: err.message,
          }
        } else if (err.request) {
          // client never received a response, or request never left
          this.error = {
            title: "Unable to Reach Server",
            message: err.message,
          }
        } else {
          this.error = {
            title: "Application Error",
            message: err.message,
          }
        }
      }
      this.loading = false
    },
  },
  mounted() {
    this.fetchGroups()
  },
}
</script>
