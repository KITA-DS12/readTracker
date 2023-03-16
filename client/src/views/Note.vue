<script setup>
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';
import axios from 'axios';

const router = useRouter()

const createDialog = ref(false)
const updateDialog = ref(false)

const title = ref("")
const content = ref("")
const textRules = [
                      v => !!v || '入力してください',
                  ]

const user_id = sessionStorage.getItem('user_id')
const user_name = sessionStorage.getItem('user_name')
if (user_id == null || user_name == null) {
  router.push('/signin')
}

const notes = ref([])

const createNote = async () => {
  await axios
    .post(`/note/${user_id}`, {
      title: title.value,
      content: content.value,
    })
    .then((res) => {
      readNotes()
      createdialog.value = false
      title.value = ""
      content.value = ""
    })
    .catch((err) => {
      console.log(err)
    })
}

const readNotes = async () => {
  await axios.get(`/notes/${user_id}`)
    .then((res) => {
      notes.value = res.data
    })
    .catch((error) => {
      console.log(error)
   })
}

const deleteNote = async (note_id) => {
  await axios.delete(`/note/${note_id}`)
    .then((res) => {
      readNotes()
    })
    .catch((error) => {
      console.log(error)
      readNotes()
   })
}

const tmp_title = ref("")
const tmp_content = ref("")
const evacuateNote = (note) => {
  tmp_title.value = note.title
  tmp_content.value = note.content
}

const updateNote = async (note) => {
  await axios
    .put(`/note/update`, {
       title: tmp_title.value,
       content: tmp_content.value,
       id: note.id,
       created_at: note.created_at,
       owner_id: user_id,
    })
    .then((res) => {
      readNotes()
      updateDialog.value = false
      tmp_title.value = ""
      tmp_content.value = ""
    })
    .catch((err) => {
      console.log(err)
    })
}

onMounted(() => {
  readNotes()
})
</script>

<template>
  <v-card min-width="350px" style="width: 80%;">
    <v-card-title
      class="text-blue-grey-darken-2
             font-weight-bold
             pa-5
             d-flex
             flex-row
             justify-space-between"
    >
      <div />
      Note
      <v-dialog
        v-model="createDialog"
        width="auto"
      >
        <template v-slot:activator="{ props }">
          <v-btn
            icon="mdi-plus"
            color="indigo"
            v-bind="props"
          />
        </template>
        <v-card max-width="600px" min-width="350px" style="width: 40%;">
          <v-card-title class="text-blue-grey-darken-2 font-weight-bold pa-5">
            New Note
          </v-card-title>
          <v-divider />
          <v-card-text class="pa-5">
              <v-form>
                  <v-text-field
                    :rules="textRules"
                    v-model="title"
                    label="タイトル"
                    variant="outlined"
                    required
                  />
                  <v-textarea
                    :rules="textRules"
                    v-model="content"
                    label="メッセージ"
                    variant="outlined"
                    maxlength="140"
                    required
                  />
                  <v-card-actions class="justify-center pa-3">
                    <v-btn
                      @click="createNote"
                      :disabled="!title || !content"
                      color="info"
                      class="font-weight-bold text-h6"
                      flat
                    >
                      送信
                    </v-btn>
                  </v-card-actions>
              </v-form>
          </v-card-text>
        </v-card>
      </v-dialog>
    </v-card-title>
    <v-divider />
    <v-table height="300px">
      <thead>
        <tr>
          <th class="text-left">
            Title
          </th>
          <th class="text-left">
            Content
          </th>
          <th class="text-left" width="130px">
            Action
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="note in notes"
          :key="note.title"
        >
          <td>{{ note.title }}</td>
          <td>{{ note.content }}</td>
          <td width="130px">
            <v-dialog
              v-model="updateDialog"
              width="auto"
            >
              <template v-slot:activator="{ props }">
                <v-btn
                  @click="evacuateNote(note)"
                  style="margin-right: 10px;"
                  variant="outlined"
                  icon="mdi-pencil"
                  color="green"
                  size="small"
                  v-bind="props"
                  flat
                />
              </template>
              <v-card max-width="600px" min-width="350px" style="width: 40%;">
                <v-card-title class="text-blue-grey-darken-2 font-weight-bold pa-5">
                  Update Note
                </v-card-title>
                <v-divider />
                <v-card-text class="pa-5">
                    <v-form>
                        <v-text-field
                          :rules="textRules"
                          v-model="tmp_title"
                          label="タイトル"
                          variant="outlined"
                          required
                        />
                        <v-textarea
                          :rules="textRules"
                          v-model="tmp_content"
                          label="メッセージ"
                          variant="outlined"
                          maxlength="140"
                          required
                        />
                        <v-card-actions class="justify-center pa-3">
                          <v-btn
                            @click="updateNote(note)"
                            :disabled="!tmp_title || !tmp_content"
                            color="info"
                            class="font-weight-bold text-h6"
                            flat
                          >
                            更新
                          </v-btn>
                        </v-card-actions>
                    </v-form>
                </v-card-text>
              </v-card>
            </v-dialog>
            <v-btn
              @click="deleteNote(note.id)"
              variant="outlined"
              icon="mdi-delete"
              color="red"
              size="small"
              flat
            />
          </td>
        </tr>
      </tbody>
    </v-table>
  </v-card>
</template>
