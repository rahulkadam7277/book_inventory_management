<template>
  <div>
    <div class="row">
      <div class="col-3"></div>
      <div class="col-6">
        <div class="card">
          <div class="card-body">
            <div class="card-title text-center font-weight-bold p-3">
              Book Details
            </div>
            <div class="from-group">
              <label for="title">ID</label>
              <input
                v-model="book.id"
                type="text"
                name="name"
                class="form-control"
                placeholder="Enter ID from google book"
              />
            </div>

            <div class="from-group">
              <label for="title">Book_Count</label>
              <input
                v-model="book.new_count"
                type="text"
                name="name"
                class="form-control"
                placeholder="Enter book count "
              />
            </div>



            <div class="form-group pt-4 text-right">
              <button class="btn btn-primary" @click="submitData()">{{isUpdate ? 'Update Book':'Add Book'}}</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      book: {
        title: "",
        description: "",
        author: "",
      },
      isUpdate: false,
    };
  },
  mounted() {
    if (this.$route.params.bookId && this.$route.params.bookId != "") {
      this.isUpdate = true;
      axios
        .post("http://localhost:8080/api/searchbookbyid", {
          id: this.$route.params.bookId,
        })
        .then((resp) => {
          console.log("data :", resp.data);
          this.book = resp.data[0];
        });
    }
  },
  methods: {
    submitData() {
        if(this.isUpdate){
            this.updateBook()
        }else{
            this.addBook()
        }
    },
    updateBook() {
      axios
        .post("http://localhost:8080/api/edit", this.book)
        .then(() => {
          alert("Update sucessfully");
        })
        .catch((error) => {
          console.log("Get bool error: ", error);
        });
    },
    addBook() {
      axios
        .post("http://localhost:8080/api/create", this.book)
        .then(() => {
          alert("Book Added sucessfully");
          this.$route.push("/")
        })
        .catch((error) => {
          console.log("Get bool error: ", error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
</style>