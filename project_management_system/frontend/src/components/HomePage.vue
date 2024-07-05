<template>
  <v-data-table :headers="headers" :items="items"></v-data-table>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: [],
      headers: [
        { text: 'Name', value: 'name' },
        { text: 'Description', value: 'description' },
      ],
    };
  },
  mounted() {
    this.fetchProjects();
  },
  methods: {
    async fetchProjects() {
      try {
        const response = await axios.get('http://localhost:8000/api/projects/');
        this.items = response.data;
      } catch (error) {
        console.error("Error: ", error);
      }
    },
  },
};
</script>
