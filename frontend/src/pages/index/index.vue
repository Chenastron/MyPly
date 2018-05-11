<template>
  <div id="index-wrapper">
    <div id="cover"></div>
    <Header/>
    <Content/>
    <Footer/>
  </div>
</template>

<script>
import Header from './components/header.vue'
import Footer from './components/footer.vue'
import Content from './components/content.vue'

export default {
  components: {
    Header,
    Footer,
    Content
  }
}
</script>

<style lang="stylus" scoped>
  #index-wrapper
    position absolute
    left 0
    right 0
    top 0
    bottom 0
  #cover
    position absolute
    left 0
    top 0
    right 0
    bottom 0
    background-color #999
    opacity .9
    z-index -1
</style>
