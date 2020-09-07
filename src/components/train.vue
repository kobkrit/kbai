<template>
  <div style="height: 100vh; width: 100vw;">
    <b-input-group class="train-panel">
      <b-input-group-prepend>
        <b-button class="btn-create" variant="primary" @click="onCreate"
          >Create</b-button
        >
      </b-input-group-prepend>
      <b-form-input class="input-url" v-model="url" placeholder="Put Google Colab URL here . . ."></b-form-input>
      <b-input-group-append>
        <button
          class="btn base-btn"
          :disabled="trainable"
          @click="onTrain()"
        >
          <b-spinner v-if="loading" small type="grow"></b-spinner
          >{{ isTraining ? "Train" : "Train" }}
        </button>
        <button
          class="btn base-btn"
          :disabled="!downloadable"
          @click="downloadAndExtract"
        >
          <b-spinner v-if="isDownloading" small type="grow"></b-spinner
          >Download
        </button>
      </b-input-group-append>
    </b-input-group>
    <b-card no-body class="train-pgr">
      <div class="bg-secondary text-light px-3 py-2 scroll-box" ref="logsBox">
        training result:<br />
        <div v-html="result" />
        <div v-html="logs" />
      </div>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

var axiosInstance = axios.create({
  baseURL: `${location.protocol}//${location.hostname}:80`,
});

export default {
  name: "Training",
  components: {},
  props: {},
  created() {},
  data() {
    return {
      url: "",
      file: null,
      result: "",
      logs: "",
      loading: false,
      polling: null,
      lastState: "",
      isDone: false,
      isTraining: false,
      isDownloading: false,
    };
  },
  methods: {
    onCreate: () => {
      window.open(
        "https://colab.research.google.com/drive/1i8vTzvrm-snMGM5v4HpcuzkdtjmtraFy",
        "_blank"
      );
    },
    prepareData: function() {
      this.result += `Preparing data ... <br />`;
      return axiosInstance.post(
        "/archiveFile",
        { path: this.getProjectDir },
        {
          responseType: "arraybuffer",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
    },
    checkRunning: function() {
      return axios.get(`${this.url}/train/is_running`);
    },
    stopTraining: function() {
      return axios.get(`${this.url}/train/stop`);
    },
    getLogs: function() {
      return axios.get(`${this.url}/train/log`);
    },
    downloadAndExtract: async function() {
      this.isDownloading = true;
      const model = await axios.get(`${this.url}/download`, {
        responseType: "arraybuffer",
      });
      var file = new File([model.data], "model.tar.gz", {
        type: "application/gzip",
      });
      let formData = new FormData();
      formData.append("file", file);
      formData.append("path", this.getProjectDir);
      await axiosInstance.post("/extractFile", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      this.isDownloading = false;
    },
    onTrain: async function() {
            axiosInstance.post("/upload", {
                projectpath: this.$store.state.projectDir
            }).then((response) => {
                console.log(response.data.status);
                this.isDone = true
                

            });
    },
  },
  directives: {},
  mounted() {},
  updated() {
    var logsBox = this.$refs.logsBox;
    logsBox.scrollTop = logsBox.scrollHeight;
  },
  computed: {
    ...mapGetters([
      "getProjectDir",
      "getProjects",
      "getImages",
      "getProjectStatus",
      "getCmdVel",
    ]),
    trainable: function() {
      const regex = new RegExp(
        /^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w.-]+)+[\w\-._~:/?#[\]@!$&'()*+,;=.]+$/
      );
      return this.url === "" || !regex.test(this.url) || this.loading;
    },
    variantType: function() {
      return this.isTraining ? "primary" : "outline-primary";
    },
    downloadable: function() {
      return this.isDone && !this.isDownloading;
    },
  },
};
</script>

<style lang="scss" scoped>
$primary-color: #007e4e;
.train-panel {
  padding: 20px;
  background: #fff;
  height: 78px;
}
.btn-create {
  border-radius: 10px 0 0 10px !important;
}
.input-url {
  border-radius: 0 10px 10px 0 !important;
}
.base-btn {
  color: white;
  background-color: $primary-color;
  margin-left: 10px !important;
  border-radius: 10px !important;
  &:disabled {
    opacity: 0.7;
  }
}
.train-pgr {
  border: none !important;
}
.scroll-box {
  height: calc( 100vh - 78px );
  overflow-y: scroll;
  text-align: left;
  padding: 20px !important;
  background-color: #333 !important;
}
</style>