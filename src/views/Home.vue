<template>
  <div class="container">
    <div class="">
    <div class="d-flex justify-content-between">
        <h4 class="font-weight-bold text-left text-uppercase pointer" @click="getInventoryBooks()">
        Inventory Books
      </h4>
    <p>
      <router-link
      class="btn btn-primary"
                :to="{
                  name: 'addBook',                 
                }"
              >
                Add Book
              </router-link>
    </p>
    </div>
    <div class="row">
      <div class="col-8">
        <div class="form-group">
         <input
                v-model="search"
                type="text"
                name="name"
                class="form-control"
                placeholder="search here ..."
              />
        </div>
      </div>
      <div class="col-3">
        <button class="btn btn-secondary" @click="searchBook()">Search</button>

      </div>
    </div>
      <div class="row">
        <div class="col-sm-6 col-md-4 col-lg-3" v-for="(book,i) in books" :key="i">         
          <BookDetails :book="book" :isSearch="isSearch" />
        </div>
      </div>
    
    </div>
  </div>
</template>

<script>
import axios from "axios";
import BookDetails from "../components/BookDetails";
// axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
export default {
  name: "Home",   
  data() {
    return {
      currentPage: 1,
      books:[],
      search:'',
      isSearch:false
    };
  },
  components: {
    BookDetails
  }, 
 created(){
   axios.get("http://localhost:8080/api/selectgener").then(resp => {
      this.books= resp.data
      this.isSearch = false
    }).catch(error => {
      console.log("Get bool error: ",error)
      this.books=[]
    })
 },
 methods: {
   searchBook(){
     this.isSearch = true
      axios.post("http://localhost:8080/api/searchbook",{book_name:this.search}).then(resp => {
      this.books= resp.data
      
    }).catch(error => {
      console.log("Get bool error: ",error)
      this.books=[]
    })

   },
   getInventoryBooks(){
      axios.get("http://localhost:8080/api/selectgener").then(resp => {
      this.books= resp.data
      this.isSearch = false
    }).catch(error => {
      console.log("Get bool error: ",error)
      this.books=[]
    })
   }
 },
};
</script>
<style lang="scss">
  .pointer{
    cursor: pointer;
  }
</style>
