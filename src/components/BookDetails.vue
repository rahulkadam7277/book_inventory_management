<template>
  <div>
    <a :href="book.previewLink">
    <div class="card movie-card">
      <div class="image">
        <div class="wrapper">
          <img
            v-if="book.imageLink"
            class="image"
            :src="book.imageLink"
            :alt="book.title"
          />
          <div v-else class="no-image"></div>
        </div>
      </div>
      <div class="content">
        <h2>
          <a>{{ book.title }}</a>
        </h2>
        <p>
          <i class="fa fa-calendar" aria-hidden="true"></i>
          {{ book.release_date }}
        </p>

        <p>
          <i class="fa fa-star" aria-hidden="true"></i>
          <span class="rating-count">{{ book.averageRating }}</span
          >/10
        </p>
        <p>
          <i class="fa fa-thumbs-up" aria-hidden="true"></i>
          {{ book.isAvailable }}
        </p>
        <p v-if="!isSearch">
          <i
            @click="deleteBook(book.bookID)"
            class="fa fa-trash icon text-danger"
            aria-hidden="true"
          />
          <!-- <i
            @click="updateBook(book.bookID)"           
            class="fa fa-pencil-square icon text-warning pl-3" aria-hidden="true"
          /> -->
          <router-link
            :to="{
              name: 'updateBook',
              params: { bookId: book.bookID },
            }"
          >
            <i
              class="fa fa-pencil-square icon text-warning pl-3"
              aria-hidden="true"
            />
          </router-link>
        </p>
      </div>
    </div>
    </a>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "BookDetails",
  props: {
    book: Object,
    default: {},
    isSearch:Boolean
  },
  methods: {
    deleteBook(bookId) {
      console.log("Delete :", bookId);
      console.log("Hello")
      axios
        .post("http://localhost:8080/api/delete", { id: bookId })
        .then(() => {
          alert("Book Deleted sucessfully");
        })       
        console.log("done")
    },
    updateBook(bookId) {
      console.log("Update ", bookId);
      this.$router.push({
        name: "course-detail",
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.movie-card {
  flex-wrap: wrap;
  align-content: flex-start;
  border: 1px solid #e3e3e3;
  overflow: hidden;
  margin-top: 30px;
  border-radius: 10px;

  .image {
    max-height: 300px;
    .wrapper {
      width: 100%;
      height: 100%;
      position: relative;
      top: 0;
      left: 0;
      .image {
        display: inline-block;
        width: 100%;
        height: 100%;
        img {
          width: 100%;
          height: 100%;
        }
      }
    }
  }
  .content {
    width: 100%;
    padding: 26px 10px 12px 10px;
    position: relative;
    white-space: normal;
    display: flex;
    align-content: flex-start;
    flex-wrap: wrap;
    h2 {
      font-size: 1em;
      margin: 0;
      width: 100%;
      text-align: left;
      word-wrap: normal;
      overflow-wrap: break-word;
      margin-bottom: 5px;
      a {
        font-weight: 700;
        color: #000;
        text-decoration: none;
      }
    }
    p {
      font-size: 1em;
      margin: 0;
      padding: 5px 10px 0px 10px;
      color: rgba(0, 0, 0, 0.6);
    }
  }
}

.card {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(var(--lightGrey), 1);
  background-color: #fff;
}
.rating-count {
  font-weight: 600;
  font-size: 1rem;
}
.no-image {
  background-image: url("../assets/default.svg");
  background-color: #dbdbdb;
  background-size: 50%;
  box-sizing: border-box;
  min-height: 300px;
  max-height: 300px;
  align-items: center;
  justify-content: center;
  line-height: inherit;
  background-position: center center;
  background-repeat: no-repeat;
  color: inherit;
}
</style>
