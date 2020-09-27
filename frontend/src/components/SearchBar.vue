<template>
  <div class="hello">
    <img alt="Vue logo" src="../assets/logo.svg" class="logo">
    <div class="container_500 search__wrapper">
      
        <input
          type="text"
          placeholder="Paste link"
          class="input__search"
          id="searchInput"
          v-model="textInput"
        />
          <a class="button__scan" @click="getList">scan</a>
    </div>
    <div id="result" class="container_500">
      <div v-for="(item, i) in imageList" v-bind:key="i">
        <ImageItem :data="item"></ImageItem>
      </div>
    </div>
  </div>
</template>

<script>
import ImageItem from "./ImageItem.vue"
import axios from 'axios'

export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  components: {
    ImageItem
  },
  data(){
    return {
      textInput: null,
      item: {
        "width": 100,
        "height": 100,
        "ext": "jpeg",
        "size": "100 kB",
        "url": "https://zastava-ermaka.ru/storage/app/media/uploaded-files/i.jpg"
      },
      imageList: null,
      error: null,
    }
  },
  methods: {
    async getList(){
      try{
        await axios.post(`http://127.0.0.1:5000/api/images/get`, {"url": this.textInput}).then((response)=> {
          this.imageList = null
          if(response.data.length == 0){
            this.error = "No Data"  
          } else {
            this.imageList = response.data
          }
        })
      } catch(e) {
        this.error = e
      }
      
    }
  }
};
</script>

<style scoped lang="scss">
.error_bar{
  position: fixed;
  bottom: 0;
  height: 40px;
  width: 100%;
  background: rgba(red, .2);
  animation: fadeOut 5s ease-out;
}
@keyframes fadeOut{
  99%{
    opacity: 0;
  }
  100%{
    display: none;
  }
}
.search__wrapper {
  margin-top: 15px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.search__container {
  display: flex;
 
  
}
.input__search {
  width: 100%;
  border: none;
  border-radius: 10px 0px 0px 10px;
  border: 1px solid #eee;
  height: 100%;
  box-sizing: border-box;
  padding: 15px 20px;
  transition: .2s;
  &:focus{
    outline: none;
    border: 1px solid #656CA8;
  }
}
.button__scan {
  background-color: #656CA8;
  padding: 0px 20px;
  border-radius: 0px 10px 10px 0px;
  color: #fff;
  display: block;
  height: 100%;
  line-height: 40px;
  cursor: pointer;
}
.logo{
  margin-top: 15px;
}
</style>
