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
          @click="onTrain()"
        >Train
        </button>
        <button 
          class="btn base-btn"
          @click="downloadAndExtract"
        >
        Test Detection
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
      



  	 <b-modal id="myModalId" size="xl" title="Detected image" ok-only ok-variant="secondary" ok-title="Dismiss" >
			<img :src="imageData" />
	 </b-modal>


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
      imageData : null ,
      showModal: false,
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


   
    downloadAndExtract:  function() {
      console.log("Now loading!!!!")
            axiosInstance.post("/detect", {
                projectpath: this.$store.state.projectDir,
                filename : "1569404476961.png"
            }).then((response) => {
    
      /*       let blob = new Blob(
        [response.data], 
        { type: response.headers['content-type'] }
      ) */

            //const urlCreator = window.URL || window.webkitURL;
            //var b64Response = btoa(unescape(encodeURIComponent(response.data)))
            var str = response.data.ImageBytes

        
             
              //this.imageData = url.createObjectURL(blob);


              
                var base64data = str;    
                //this.imageData = base64data          
                console.log(base64data);
                   //console.log(this.imageData)
                   this.imageData = 'data:image/png;base64,' + base64data;
              console.log("get response")
              this.showModal = true
              this.$root.$emit('bv::show::modal', 'myModalId')
         
           
            
          
            //this.imageData = 'data:image/png;base64,' + b64Response;
            //this.imageData = urlCreator.createObjectURL(blob);

            //console.log(this.imageData)
       
            //return this.imageData 

            });
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
  mounted() {
      

  },
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