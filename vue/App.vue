<template>

  <div class="black-bg" v-if="모달창열렸니 == true">
      <div class="white-bg">
        <h4>상세페이지임</h4>
        <p>상세페이지 내용임</p>
      </div>
      <button @click="모달창열렸니=false">닫기</button>
  </div>

  <div class="menu">
    <a>Home</a>
    <a>Products</a>
    <a v-for="a in 메뉴들" :key="a">{{a}}</a>
  </div>
  
  <div v-for="(a,i) in 원룸들" :key="i">
    <img :src="원룸들[i].image" alt="" class="room-img"> 
    <h4 class="red" :style="스타일" @click="모달창열렸니=true">{{원룸들[i].title }}</h4>
    <p>{{원룸들[i].price }}원</p>
    <button @click="신고수[i]++">허위매물신고</button> <span>신고수 : {{신고수[i]}}}</span><br>
    <button @mouseover="신고수[i]++">허위매물신고</button> <span>신고수 : {{신고수[i]}}}</span><br>
    <button @click="increase(i)">허위매물신고</button> <span>신고수 : {{신고수[i]}}}</span><br>
  
  </div>
</template>

<script>

import data from './assets/oneroom.js';


export default {
  name: 'App',
  data(){
    return{
      원룸들 : data,
      신고수 : [0,0,0,0,0,0],
      모달창열렸니 : false,
      스타일 : 'color : blue',
      products : ['역삼동원룸','천호동원룸','마포구원룸'],
      메뉴들 : ['Home','Shop','About'],
    }
  },
  methods: {
    increase(i){
      this.신고수[i]++;
    },
  },
  components: {
    
  }
}
</script>

<style>
body{
  margin:0;
}
div{
  box-sizing: border-box;
}
.black-bg{
  width:100%; height: 100%;
  background: rgba(0,0,0,0.5);
  position: fixed; padding: 20px;
}
.white-bg{
  width:100%;
  background: white;
  border-radius: 8px;
  padding: 20px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.menu{
  background: darkslateblue;
  padding: 15px;
  border-radius: 5px;
}
.menu a{
  color: white;
  padding:10px;
}
.room-img{
  width: 100%;
  margin-top: 40px;
}
</style>
