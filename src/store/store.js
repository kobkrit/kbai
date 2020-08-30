import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'

Vue.use(Vuex)

var axiosInstance = axios.create({
  baseURL: `${location.protocol}//${location.hostname}:80`,
})

export default new Vuex.Store({
  state: {
    projectDir: 'None', // The TV inventory
    projects: [],
    images: [],
    isProjectOpen: false,
    sCmdVel: null,
    trainingType: 'None',
    blockly_workspace: null,
    blockly_xml: "",
    usb_path:"",
    rbServer: undefined,
  },

  getters: {
    // Here we will create a getter
    getProjectDir: (state) => {
      return state.projectDir
    },
    getProjects: (state) => state.projects,
    getImages: (state) => state.images,
    getProjectStatus: (state) => state.isProjectOpen,
    getCmdVel: (state) => state.sCmdVel,
    getTrainingType: (state) => state.trainingType,
    getBlocklyWorkspace: state => state.blockly_workspace,
    getBlocklyXml: state => state.blockly_xml,
    getUsbPath: state => state.usb_path,
    getRbServer: state => state.rbServer,
  },

  mutations: {
    setProjectDir(state, proDir) {
      state.projectDir = proDir
    },
    addPeojects(state, projects) {
      state.projects = projects
    },
    addImages(state, images) {
      state.images = images
    },
    setCmdVel(state, cmd) {
      state.sCmdVel = cmd
    },
    setTrainingType(state, type) {
      state.trainingType = type
    },
    setBlocklyWorkspace(state, blockly_workspace){
      console.log("<============ Set workspace =============>")
      state.blockly_workspace = blockly_workspace
    },
    setBlocklyXml(state, blockly_xml){
      console.log("<============ Store =============>")
      console.log(blockly_xml)
      state.blockly_xml = blockly_xml
    },
    setUsbPath(state, path){
      state.usb_path = path
    },
    setRbServer(state, rbServer){
      state.rbServer = rbServer
    }
  },

  actions: {
    // Here we will create Larry
    setProjectDir(context, proDir) {
      axiosInstance
        .post('createProject', {
          projectDir: proDir,
        })
        .then((response) => {
          console.log(response.data)
          if (response.data.status === 'OK') {
            console.log('File is OK!!!!')
            context.commit('setProjectDir', proDir)
          }
        })
        .catch((error) => {
          console.log(error)
        })
    },
    changeProjectDir(context, proDir) {
      context.commit('setProjectDir', proDir)
    },
    uploadImage({ state, dispatch }, imgData) {
      axiosInstance
        .post('/upload/image', {
          path: state.projectDir,
          base64image: imgData,
        })
        .then((response) => {
          console.log(response.data)
          if (response.data.status === 'OK') {
            console.log('File is OK!!!!')

            //this.$refs['saveAnotation'].show()
            dispatch('reqImages')
            //return true;
          }
        })
        .catch((error) => {
          console.log(error)
          //return false;
        })
    },
    regProjects(context) {
      axiosInstance
        .get('/getProjects')
        .then((response) => {
          console.log(response.data)
          if (response.data.status === 'OK') {
            console.log('File is OK!!!!')
            context.commit('addPeojects', response.data.projects)
            context.state.isProjectOpen = true

            //this.$refs['saveAnotation'].show()

            //return true;
          }
        })
        .catch((error) => {
          console.log(error)
          //return false;
        })
    },
    reqImages({ state, commit }) {
      let uri = '/getFiles'
      console.log(state.projectDir)
      axiosInstance
        .post(uri, {
          path: state.projectDir,
        })
        .then((response) => {
          var info = response.data.files
          var index, len
          var allImgs = []
          for (index = 0, len = info.length; index < len; ++index) {
            var imPath =
              '/' +
              info[index].file
            allImgs.push({
              fileName: info[index].file,
              file: imPath,
              id: info[index].id,
            })
          }
          console.log(response.data.files)
          commit('addImages', allImgs)
        })
    },
    setCmdVel({ state }, cmd) {
      state.sCmdVel = cmd
    },

    deleteProject({ state, commit }, sel_projectDir) {
      let uri = '/deleteProject'
      console.log(sel_projectDir)
      axiosInstance
        .post(uri, {
          path: sel_projectDir,
        })
        .then((response) => {
          console.log(response.data)
          console.log(sel_projectDir)
          console.log(state.projectDir)
          if (sel_projectDir === state.projectDir) {
            commit('setProjectDir', 'null')
          }
        })
    },

    setTrainingType(context, type) {
      context.commit('setTrainingType', type)
    },

    setBlocklyXml({ commit }, blockly_xml) {
      commit('setBlocklyXml', blockly_xml);
    },
    
    clearBlocklyWorkspace({state}){
      console.log("<===== Clear workspace =====>")
      state.blockly_workspace.clear()
    }
  },
})
