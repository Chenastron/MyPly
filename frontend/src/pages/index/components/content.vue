<template>
  <div id="content-wrapper">
    <div class="input-title">
      <el-select v-model="selectedValue" placeholder="请选择">
        <el-option
          v-for="item in inputOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-button type="primary" plain @click="commitInput">
        运行
      </el-button>
    </div>
    <div class="input-wrapper">
      <el-input
        class="input"
        type="textarea"
        :rows="20"
        placeholder="请输入内容"
        v-model="inputArea">
      </el-input>
      <el-input
        class="output"
        type="textarea"
        :rows="20"
        :disabled="true"
        v-model="outputArea">
      </el-input>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'

export default {
  name: 'Content',
  data () {
    return {
      inputOptions: [
        {
          label: '词法分析',
          value: 'lex'
        },
        {
          label: '语法分析',
          value: 'yacc'
        },
        {
          label: '执行结果',
          value: 'exe'
        }
      ],
      selectedValue: 'exe',
      inputArea: '',
      outputAreaDatas: ''
    }
  },
  computed: {
    outputArea () {
      return this.outputAreaDatas[this.selectedValue]
    }
  },
  methods: {
    commitInput () {
      axios({
        method: 'post',
        url: 'api/',
        data: qs.stringify({
          string: this.inputArea
        }),
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        }
      }).then(this.getInfoSucc)
    },
    getInfoSucc (res) {
      this.outputAreaDatas = res.data
    }
  }
}
</script>

<style scoped lang="stylus">
#content-wrapper
  padding 0 10vw
  display flex
  justify-content space-between
  flex-direction column
  .input-title
    width 48%
    display flex
    justify-content space-between
    margin-bottom 2vh
  .input-wrapper
    display flex
    justify-content space-between
    width 100%
    .input
      width 48%
    .output
      width 48%
</style>
