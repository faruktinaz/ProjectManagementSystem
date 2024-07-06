<template>
  <v-container>
    <v-row justify="center">
      <v-btn color="primary" class="px-6 my-12" @click="openNewProjectDialog"
        >Yeni Proje Ekle</v-btn
      >
    </v-row>

    <v-data-table
      :headers="headers"
      :items="items"
      item-value="id"
      show-expand
      class="elevation-1"
    >
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon small @click="editProject(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteProject(item.id)">mdi-delete</v-icon>
      </template>
    </v-data-table>

    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">{{
            isEdit ? "Projeyi Düzenle" : "Yeni Proje Ekle"
          }}</span>
        </v-card-title>
        <v-card-text>
          <v-form ref="form">
            <v-text-field v-model="editItem.name" label="Name"></v-text-field>
            <v-text-field
              v-model="editItem.description"
              label="Description"
            ></v-text-field>
            <v-text-field v-model="editItem.slug" label="Slug"></v-text-field>
            <v-text-field
              v-model="editItem.language"
              label="Language"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false"
            >İptal</v-btn
          >
          <v-btn
            color="blue darken-1"
            text
            @click="isEdit ? updateProject() : createProject()"
          >
            {{ isEdit ? "Kaydet" : "Ekle" }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  setup() {
    const items = ref([]);
    const dialog = ref(false);
    const isEdit = ref(false);
    const editItem = ref({
      id: "",
      name: "",
      description: "",
      slug: "",
      language: "",
    });
    const headers = ref([
      { title: "ID", key: "id" },
      { title: "Name", key: "name" },
      { title: "Description", key: "description" },
      { title: "Slug", key: "slug" },
      { title: "Language", key: "language" },
      { title: "Repositories", key: "repositories" },
      { title: "Trackers", key: "trackers" },
      { title: "Actions", key: "actions", sortable: false },
    ]);

const fetchProjects = () => {
    axios.get("http://localhost:8000/api/projects/")
        .then((response) => {
            const updatedData = response.data.map(item => {
                if (item.repositories.length > 0)
				{
                    item.repositories = item.repositories.map(repo => {
                        return `ID: ${repo.id}, Title: ${repo.title}, URL: ${repo.url}, Type: ${repo.type}, Email: ${repo.email}, Token: ${repo.token}, Project: ${repo.project}`;
                    }).join(' | ');
                } else 
                    item.repositories = "No repositories";
				if (item.trackers.length > 0)
				{
					item.trackers = item.trackers.map(track => {
						return `ID: ${track.id}, Title: ${track.title}, URL: ${track.url}, Type: ${track.type}, Email: ${track.email}, Token: ${track.token}, Project: ${track.project}`;
					}).join(' | ')
				} else {
					item.trackers = "No Trackers"
				}
                return item;
            });

            items.value = updatedData;
            console.log(items.value);
        })
        .catch((error) => {
            console.log(error);
        });
};

    const deleteProject =  (id) => {
        axios.delete(`http://localhost:8000/api/projects/${id}/`).then((res) => {
			items.value = items.value.filter((item) => item.id !== id);
			console.log(res);
		}).catch((err) => {
			console.log(err);
		});
    };

    const editProject = (item) => {
      editItem.value = { ...item };
      isEdit.value = true;
      dialog.value = true;
    };

    const openNewProjectDialog = () => {
      editItem.value = {
        id: "",
        name: "",
        description: "",
        slug: "",
        language: "",
      };
      isEdit.value = false;
      dialog.value = true;
    };

    const updateProject = () => {
      axios
        .put(
          `http://localhost:8000/api/projects/${editItem.value.id}/`,
          editItem.value
        )
        .then((res) => {
          console.log(res);
          const index = items.value.findIndex(
            (item) => item.id === editItem.value.id
          );
          if (index !== -1) {
            items.value.splice(index, 1, { ...editItem.value });
          }
          dialog.value = false;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const createProject = () => {
      axios
        .post("http://localhost:8000/api/projects/", editItem.value)
        .then((res) => {
          items.value.push(res.data);
          dialog.value = false;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    onMounted(() => {
      fetchProjects();
    });

    return {
      items,
      headers,
      dialog,
      isEdit,
      editItem,
      deleteProject,
      editProject,
      openNewProjectDialog,
      updateProject,
      createProject,
    };
  },
};
</script>
