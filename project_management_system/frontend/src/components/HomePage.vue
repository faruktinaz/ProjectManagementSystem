<template>
  <div class="main-container">
    <div class="bottom-container">
      <v-row justify="center">
        <v-btn color="primary" class="px-6 my-12" @click="openNewProjectDialog"
          >Yeni Proje Ekle</v-btn
        >
      </v-row>

      <v-data-table
        :headers="headers"
        :items="items"
        item-value="id"
        class="elevation-24 rounded-lg py-6 px-6"
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
              <v-card class="mb-4">
                <v-card-title>Repositories</v-card-title>
                <v-card-text>
                  <v-row>
                    <v-col>
                      <v-text-field
                        v-model="editItem.repository_title"
                        label="Repo Title"
                      >
                      </v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="editItem.repository_url"
                        label="Repo URL"
                      >
                      </v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="editItem.repository_email"
                        label="Repo Email"
                      >
                      </v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-select
                        v-model="editItem.repository_type"
                        label="Repo Type"
                        :items="typeItems"
                      >
                      </v-select>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="editItem.repository_token"
                        label="Repo Token"
                      >
                      </v-text-field>
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>
              <v-card class="mb-4">
                <v-card-title>Trackers</v-card-title>
                <v-card-text>
                  <v-row>
                    <v-col>
                      <v-text-field
                        v-model="editItem.tracker_title"
                        label="Track Title"
                      >
                      </v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="editItem.tracker_url"
                        label="Track URL"
                      >
                      </v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="editItem.tracker_email"
                        label="Track Email"
                      >
                      </v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-select
                        v-model="editItem.tracker_type"
                        label="Track Type"
                        :items="typeItemsTrack"
                      >
                      </v-select>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="editItem.tracker_token"
                        label="Track Token"
                      >
                      </v-text-field>
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>
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
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  setup() {
    const items = ref([]);
    const typeItems = ref(["github", "gitlab", "bitbucket"]);
    const typeItemsTrack = ref(["github", "gitlab", "jira"]);
    const dialog = ref(false);
    const isEdit = ref(false);
    const editItem = ref({
      id: "",
      name: "",
      description: "",
      slug: "",
      language: "",
      repository_title: "",
      repository_url: "",
      repository_type: "",
      repository_email: "",
      repository_token: "",
      tracker_title: "",
      tracker_url: "",
      tracker_type: "",
      tracker_email: "",
      tracker_token: "",
    });
    const headers = ref([
      { title: "Actions", key: "actions", sortable: false },
      { title: "ID", key: "id" },
      { title: "Name", key: "name" },
      { title: "Description", key: "description" },
      { title: "Slug", key: "slug" },
      { title: "Language", key: "language" },
      { title: "Repo title", key: "repository_title" },
      { title: "Repo Url", key: "repository_url" },
      { title: "Repo Type", key: "repository_type" },
      { title: "Repo Email", key: "repository_email" },
      { title: "Repo Token", key: "repository_token" },
      { title: "Tracker title", key: "tracker_title" },
      { title: "Tracker Url", key: "tracker_url" },
      { title: "Tracker Type", key: "tracker_type" },
      { title: "Tracker Email", key: "tracker_email" },
      { title: "Tracker Token", key: "tracker_token" },
    ]);

    const fetchProjects = () => {
      axios
        .get("http://localhost:8000/api/projects/")
        .then((response) => {
          console.log(response);
          items.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const deleteProject = (id) => {
      axios
        .delete(`http://localhost:8000/api/projects/${id}/`)
        .then((res) => {
          items.value = items.value.filter((item) => item.id !== id);
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const editProject = (item) => {
      editItem.value = { ...item };
      console.log(item, "item");
      console.log(editItem, "edit item");
      isEdit.value = true;
      dialog.value = true;
    };

    const openNewProjectDialog = () => {
      editItem.value = {
        name: "",
        description: "",
        slug: "",
        language: "",
        repository_title: "",
        repository_url: "",
        repository_type: "",
        repository_email: "",
        repository_token: "",
        tracker_title: "",
        tracker_url: "",
        tracker_type: "",
        tracker_email: "",
        tracker_token: "",
      };
      isEdit.value = false;
      dialog.value = true;
    };

    const updateProject = () => {
      console.log(editItem, "update edit item");
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
      typeItemsTrack,
      typeItems,
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

<style>
.main-container {
  width: 100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.bottom-container {
	width: 92%;
}
</style>
