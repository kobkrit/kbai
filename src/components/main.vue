<template>
<div>
    <div class="container-fluid vh-100 d-flex main-bg">
        <div class="left-panel d-flex flex-column">
            <div class="l-title font-weight-bold">KidBright AI</div>
            <div class="d-inline-flex flex-wrap menu-starter">
                <div class="btn-base new" data-md-tooltip="สร้าง Project ใหม่" v-on:click="selectedMenu = 1" v-b-modal.modal-prevent-closing />
                <div data-md-tooltip="เปิด Project ที่เคยสร้างไว้แล้ว" class="btn-base open" v-on:click="getAllProjects" v-b-modal.modal_list_files />
                <!-- <b-button v-on:click="deleteProject" v-b-modal.modal_list_delete_files
            >Delete</b-button
          > -->
                <!-- <b-button
            variant="info"
            @click="loadAllFromUSB"
            :disabled="isLoading || isSaving"
          >
            <b-spinner v-if="isLoading" small></b-spinner> Import
          </b-button> -->
                <div data-md-tooltip="บันทึกข้อมูล" class="btn-base save" variant="success" @click="saveToUSB" :disabled="isLoading || isSaving">
                    <b-spinner v-if="isSaving" small />
                </div>
                <div data-md-tooltip="นำ Thumb drive ออก" class="btn-base eject" variant="danger" @click="ejectUSB" :disabled="isLoading || isSaving" />
            </div>
            <div class="left-bottom-content d-flex flex-fill">
                <div class="proj-name">
                    <span class="icon">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36.375 55.429">
                            <g id="light-bulb" transform="translate(0 0)">
                                <path id="Path_64" data-name="Path 64" d="M25.115,41.68H11.258a1.624,1.624,0,0,1-1.589-1.288c-.263-1.241-.525-2.764-.78-4.236-.152-.881-.308-1.786-.463-2.621a18.191,18.191,0,1,1,19.519,0c-.155.834-.311,1.738-.463,2.619-.254,1.473-.517,3-.78,4.236a1.624,1.624,0,0,1-1.589,1.288Zm0,0" transform="translate(0 0)" fill="#ffd222" />
                                <path id="Path_65" data-name="Path 65" d="M168,0V41.68h6.927a1.624,1.624,0,0,0,1.589-1.288c.263-1.241.526-2.763.78-4.236.152-.88.308-1.785.463-2.619A18.189,18.189,0,0,0,168,0Zm0,0" transform="translate(-149.813)" fill="#ecbd00" />
                                <path id="Path_66" data-name="Path 66" d="M96.622,372a8.67,8.67,0,0,1-8.661-8.661v-6.712A1.624,1.624,0,0,1,89.585,355h14.078a1.624,1.624,0,0,1,1.624,1.624v6.712A8.673,8.673,0,0,1,96.622,372Zm0,0" transform="translate(-78.439 -316.568)" fill="#f5f0eb" />
                                <path id="Path_67" data-name="Path 67" d="M119.253,101.727a1.624,1.624,0,0,1-1.265-2.64l4.263-5.312h-4.626a1.624,1.624,0,0,1-1.273-2.632l5.963-7.529a1.624,1.624,0,1,1,2.546,2.017l-3.878,4.9h4.653a1.624,1.624,0,0,1,1.267,2.64l-6.381,7.952A1.622,1.622,0,0,1,119.253,101.727Zm0,0" transform="translate(-103.443 -74.013)" fill="#fff16c" />
                                <path id="Path_68" data-name="Path 68" d="M79.392,418.248H58.6a1.624,1.624,0,0,1,0-3.248H79.392a1.624,1.624,0,0,1,0,3.248Zm0,0" transform="translate(-50.812 -370.073)" fill="#ebe1dc" />
                                <path id="Path_69" data-name="Path 69" d="M79.392,358.248H58.6a1.624,1.624,0,1,1,0-3.248H79.392a1.624,1.624,0,1,1,0,3.248Zm0,0" transform="translate(-50.812 -316.568)" fill="#ebe1dc" />
                                <path id="Path_70" data-name="Path 70" d="M168,89.71l3.23-4.079a1.624,1.624,0,1,0-2.546-2.016l-.685.864Zm0,0" transform="translate(-149.813 -74.013)" fill="#f2de00" />
                                <path id="Path_71" data-name="Path 71" d="M173.469,153.465a1.624,1.624,0,0,0-1.464-.921H168v3.248h.62l-.62.773v5.189l5.272-6.57A1.623,1.623,0,0,0,173.469,153.465Zm0,0" transform="translate(-149.812 -136.029)" fill="#f2de00" />
                                <path id="Path_72" data-name="Path 72" d="M175.037,355H168v17a8.673,8.673,0,0,0,8.661-8.661v-6.712A1.624,1.624,0,0,0,175.037,355Zm0,0" transform="translate(-149.813 -316.568)" fill="#ebe1dc" />
                                <g id="Group_11" data-name="Group 11" transform="translate(18.187 38.432)">
                                    <path id="Path_73" data-name="Path 73" d="M178.393,355H168v3.248h10.393a1.624,1.624,0,1,0,0-3.248Zm0,0" transform="translate(-168 -355)" fill="#dcd2cd" />
                                    <path id="Path_74" data-name="Path 74" d="M178.393,415H168v3.248h10.393a1.624,1.624,0,1,0,0-3.248Zm0,0" transform="translate(-168 -408.504)" fill="#dcd2cd" />
                                </g>
                            </g>
                        </svg>
                    </span>
                    {{ getProjectDir }}
                </div>
                <ul v-show="getProjectDir !== 'None'" class="step">
                    <!--v-show="getProjectDir !== 'None'"-->
                    <li v-bind:class="{ current: selectedMenu == 1 }" v-on:click="
                selectedMenu = 1;
                handleTabChange(selectedMenu);
              ">
                        <img src="../assets/UI/svg/Group 13.svg" alt="" srcset="" />
                    </li>
                    <li v-bind:class="{ current: selectedMenu == 2 }" v-on:click="
                selectedMenu = 2;
                handleTabChange(selectedMenu);
              ">
                        <img src="../assets/UI/svg/Group 88.svg" alt="" srcset="" />
                    </li>
                    <li v-bind:class="{ current: selectedMenu == 3, inactive: !hasImage }" v-on:click="
                if (hasImage) {
                  selectedMenu = 3;
                  handleTabChange(selectedMenu);
                }
              ">
                        <img src="../assets/UI/svg/Group 90.svg" alt="" srcset="" />
                    </li>
                    <li v-bind:class="{
                current: selectedMenu == 4,
                inactive: !finishAnnotation,
              }" v-on:click="
                if (finishAnnotation) {
                  selectedMenu = 4;
                  handleTabChange(selectedMenu);
                }
              ">
                        <img src="../assets/UI/svg/Group 89.svg" alt="" srcset="" />
                    </li>
                </ul>
                <div v-if="getTrainingType === 'None'" class="hint">
                    <div class="main-hint txt" v-bind:class="{ notype: getTrainingType === 'None' }">
                        <!-- <ul class="btn-desc">
                <li>
                  <span
                    ><img
                      src="../assets/UI/svg/Path 216.svg"
                      alt=""
                      srcset=""/></span
                  >สร้าง Project ใหม่
                </li>
                <li>
                  <span
                    ><img
                      src="../assets/UI/svg/internet.svg"
                      alt=""
                      srcset=""/></span
                  >เปิด Project ที่เคยสร้างไว้แล้ว
                </li>
                <li>
                  <span
                    ><img
                      src="../assets/UI/svg/internet-2.svg"
                      alt=""
                      srcset=""/></span
                  >บันทึกข้อมูล
                </li>
                <li>
                  <span
                    ><img
                      src="../assets/UI/svg/Path 217.svg"
                      alt=""
                      srcset=""/></span
                  >นำ Thumb drive ออก
                </li>
              </ul> -->
                        <p>
                            เริ่มใช้งานโดยกด <img src="../assets/UI/png/Group -2.png" alt="" srcset="" />เพื่อทำการเลือก <span class="p-color">Object Detection</span> หรือ <span class="p-color">Image
                                Classification</span><br><br>ในกรณีที่เลือก <span class="p-color">Object Detection</span>
                            กระบวนการสร้างโมเดล (Training) ทำบน Colab
                            จำเป็นต้องเชื่อมต่ออินเทอร์เน็ตให้เรียบร้อยก่อน<br><br>ในกรณีที่เลือก
                            <span class="p-color">Image Classification</span> กระบวนการสร้างโมเดล (Training) ทำบน
                            KidBright AI
                        </p>
                    </div>
                    <div class="mascot">
                        <img v-if="!isRunning" src="../assets/UI/svg/Mask Group 1.svg" alt="" srcset="" />
                    </div>
                </div>
                <div v-if="getTrainingType !== 'None' && selectedMenu === 1" class="hint">
                    <div class="main-hint txt">
                        <p class="p-color font-weight-bold">ขั้นตอนที่ 1 Coding</p>
                        <p>
                            ขั้นตอนนี้ใช้สร้างชุดคำสั่งโดยการลากบล็อคคำสั่งจากแถบเครื่องมือ ในกรณีที่ยังไม่มีโมเดลรู้จำต้องการทำกระบวนการสร้างโมเดล โดยมีลำดับเริ่มจาก<br><span class="p-color">ขั้นตอนที่ 2 (Capture)</span> <br><span class="p-color">ขั้นตอนที่ 3 (Annotate)</span> <br><span class="p-color">ขั้นตอนที่ 4 (Training)</span>
                        </p>
                        <p class="p-color font-weight-bold"><br>ขั้นตอนถัดไปกดปุ่ม <img src="../assets/UI/svg/Group 95.svg" alt="" srcset="" /></p>
                    </div>
                    <div class="mascot">
                        <img v-if="!isRunning" src="../assets/UI/svg/Mask Group 11.svg" alt="" srcset="" />
                        <img v-if="isRunning" src="../assets/UI/svg/Mask Group 10.svg" alt="" srcset="" />
                    </div>
                </div>
                <div v-if="getTrainingType !== 'None' && selectedMenu === 2" class="hint">
                    <div class="main-hint txt">
                        <p class="p-color font-weight-bold">ขั้นตอนที่ 2 Capture</p>
                        <p>
                            ขั้นตอนนี้เป็นการใช้งานกล้องในการเก็บภาพที่ต้องการ โดยกดปุ่ม <img src="../assets/UI/svg/Group 113.svg" alt="" srcset="" /> เพื่อถ่ายภาพ (ควรถ่ายภาพวัตถุในมุมต่างๆ ประมาณ 20 ภาพต่อวัตถุ หรือมากกว่า)</p>
                        <p class="p-color font-weight-bold"><br>ขั้นตอนถัดไป
                            กดปุ่ม <img src="../assets/UI/svg/Group -1.svg" alt="" srcset="" /></p>
                    </div>
                    <div class="mascot">
                        <img src="../assets/UI/svg/Mask Group 11.svg" alt="" srcset="" />
                    </div>
                </div>
                <div v-if="getTrainingType !== 'None' && selectedMenu === 3" class="hint">
                    <div class="main-hint txt">
                        <p class="p-color font-weight-bold">ขั้นตอนที่ 3 Annotate</p>
                        <p>ขั้นตอนนี้ใช้สำหรับกำหนดขอบเขตและระบุชื่อวัตถุ</p>
                        <p><br>1. กดปุ่ม <img src="../assets/UI/svg/Group 97.svg" alt="" srcset="" /> เพื่อตั้งชื่อใหม่ให้กับวัตถุจากนั้นกำหนดขอบเขตโดยให้วัตถุอยู่ภายในกรอบสี่เหลี่ยมที่กำหนด</p>
                        <p><br>2. กดปุ่ม <img src="../assets/UI/svg/interface.svg" alt="" srcset="" /> เมื่อต้องการใช้ชื่อที่ตั้งไว้เเล้ว จะประกฏกรอบสี่เหลี่ยมขึ้นบนภาพ <img src="../assets/UI/svg/Group 96.svg" alt="" srcset="" /> จากนั้นกำหนดขอบเขตให้วัตถุ</p>
                        <p class="p-color font-weight-bold"><br>ขั้นตอนถัดไป
                            กดปุ่ม <img src="../assets/UI/svg/Group 115.svg" alt="" srcset="" /></p>
                    </div>
                    <div class="mascot">
                        <img src="../assets/UI/svg/Mask Group 11.svg" alt="" srcset="" />
                    </div>
                </div>
                <div v-if="getTrainingType === 'Image classification' && selectedMenu === 4" class="hint">
                    <div class="main-hint txt">
                        <p class="p-color font-weight-bold">ขั้นตอนที่ 4 Training<br>(Image Classification)</p>
                        <p>ขั้นตอนนี้เป็นการนำภาพที่ Annotate มาแล้วมาสร้างโมเดลรู้จำ</p>
                        <p><br>1. กดปุ่ม <span class="p-color">Train</span> เพื่อสร้างโมเดล รอจนกระบวนการสร้างโมเดลแล้วเสร็จ</p>
                        <p><br>2. กดปุ่ม <span class="p-color">Download</span> เมื่อเสร็จขั้นตอนนี้จะปรากฏบล็อคโมเดลขึ้นในขั้นตอนที่ 1 Coding</p>
                    </div>
                    <div class="mascot">
                        <img src="../assets/UI/svg/Mask Group 11.svg" alt="" srcset="" />
                    </div>
                </div>
                <div v-if="getTrainingType === 'Object detection' && selectedMenu === 4" class="hint">
                    <div class="main-hint txt">
                        <p class="p-color font-weight-bold">ขั้นตอนที่ 4 Training<br>(Object Detection)</p>
                        <p>ขั้นตอนนี้เป็นการนาภาพที่ Annotate แล้วมาสร้างโมเดลรู้จา โดยใช้ Google Colab ในการสร้างโมเดล จึงจาเป็นต้องเชื่อมต่ออินเทอร์เน็ตให้เรียบร้อยก่อน</p>
                        <p><br>1. เลือกหน้าเว็บ Colab ที่แสดงอยู่ด้านบน ทาการ login โดยใช้ Google Account ทาตามกระบวนการที่ปรากฏ เมื่อเสร็จสิ้นทาการคัดลอก URL</p>
                        <p><br>2. เลือกหน้าเว็บ KidBright AI และนา URL ที่คัดลอกมาใส่ในกล่องสีเทา</p>
                        <p><br>3. กดปุ่ม <span class="p-color">Train</span> เพื่อส่งภาพไปสร้างโมเดลที่ Colab รอจนกระบวนการสร้างโมเดลเสร็จสิ้น</p>
                        <p><br>4. กดปุ่ม <span class="p-color">Download</span> เพื่อนาโมเดลจาก Colab มาเก็บที่ KidBright AI เมื่อเสร็จขั้นตอนนี้จะปรากฏบล็อกโมเดลขึ้นในขั้นตอนที่ 1 Coding</p>
                    </div>
                    <div class="mascot">
                        <img src="../assets/UI/svg/Mask Group 11.svg" alt="" srcset="" />
                    </div>
                </div>
            </div>
        </div>
        <div class="content-panel d-flex flex-fill">
            <BlocklyComponent ref='blocklyComponent' v-bind:is-running="isRunning" v-bind:is-project-loaded="isProjectLoaded" v-show="selectedMenu === 1" v-on:run="showCode()" v-on:stopRun="stopRun()" />
            <Capture ref='captureComponent' v-show="selectedMenu === 2" />
            <Anotate ref='anotateComponent' v-show="getTrainingType === 'Object detection' && selectedMenu === 3" />
            <AnnotateForClassify ref='anotateForClassifyComponent' v-show="getTrainingType === 'Image classification' && selectedMenu === 3" />
            <Train ref='trainComponent' v-show="getTrainingType === 'Object detection' && selectedMenu === 4" />
            <TrainLocal ref='trainLocalComponent' v-show="getTrainingType === 'Image classification' && selectedMenu === 4" />
        </div>
        <!-- <div>Right Panel</div> -->
    </div>
    <b-modal id="modal-prevent-closing" ref="modal" title="Enter project name" @show="resetModal" @hidden="resetModal" @ok="handleOk">
        <form ref="form" @submit.stop.prevent="handleSubmit">
            <b-form-group :state="nameState" label="Name" label-for="name-input" invalid-feedback="Name is required">
                <b-form-input id="name-input" v-model="projectDirIn" :state="nameState" required></b-form-input>
            </b-form-group>
            <b-dropdown id="dropdown-1" :text="
            getTrainingType !== 'None'
              ? getTrainingType
              : 'Select trainning type'
          " class="mode-select">
                <b-dropdown-item @click="handleSelect('Object detection')">Object detection</b-dropdown-item>
                <b-dropdown-item @click="handleSelect('Image classification')">Image classification</b-dropdown-item>
            </b-dropdown>
        </form>
    </b-modal>

    <b-modal id="modal_list_files" ref="openModal" title="Projects list" @show="resetOpenModal" @hidden="resetOpenModal" @ok="openProject">
        <!--<div v-for="(item, index) in projectsName" :key="`fruit-${index}`">
            {{ item }}
        </div>-->
        <b-dropdown id="dropdown-1" :text="
            getTrainingType !== 'None'
              ? getTrainingType
              : 'Select trainning type'
          " class="mode-select">
            <b-dropdown-item @click="handleSelect('None')">None</b-dropdown-item>
            <b-dropdown-item @click="handleSelect('Object detection')">Object detection</b-dropdown-item>
            <b-dropdown-item @click="handleSelect('Image classification')">Image classification</b-dropdown-item>
        </b-dropdown>
        <b-table show-empty striped hover stacked="md" caption-top selectable :select-mode="selectMode" selectedVariant="success" :items="projectsName" @row-selected="rowSelected" @row-clicked="rowClicked">
        </b-table>
    </b-modal>

    <b-modal id="modal_list_delete_files" title="Project list" @ok="handleProjectDelete">
        <b-table show-empty striped hover stacked="md" caption-top selectable :select-mode="selectMode" selectedVariant="success" :items="projectsName" @row-selected="rowDeleteSelected" @row-clicked="rowDeleteClicked">
        </b-table>
    </b-modal>

    <!-- <b-modal
      id="modal_list_usb_directories"
      title="Project list"
      @ok="loadFromUSB"
      :ok-disabled="!directorySelected"
    >
      <b-table
        show-empty
        striped
        hover
        stacked="md"
        caption-top
        selectable
        :select-mode="selectMode"
        selectedVariant="success"
        :items="projectsfromUSB"
        @row-selected="onSelectDirectory"
      >
      </b-table>
    </b-modal> -->

    <b-modal ref="pyhonLoading" hide-footer title="Loading code">
        <div class="d-block text-center">
            <b-progress :max="max" height="2rem" :striped="true" show-progress :animated="true">
                <b-progress-bar :value="value" variant="success">
                    <h5 v-if="value > 0">Loading</h5>
                </b-progress-bar>
            </b-progress>
        </div>
    </b-modal>
</div>
</template>

<script>
import axios from "axios";
import {
    mapGetters
} from "vuex";
import Anotate from "@/components/anonate.vue";
import AnnotateForClassify from "@/components/annotateForClassify.vue";
import Capture from "@/components/capture.vue";
import BlocklyComponent from "@/components/BlocklyComponent.vue";
import Train from "@/components/train.vue";
import TrainLocal from "@/components/trainLocal.vue";
import "../blocks/stocks";
import "../prompt";
// import { VueTabs, VTab } from "vue-nav-tabs";
//you can also import this in your style tag
import "vue-nav-tabs/themes/vue-tabs.css";
import "vue-awesome/icons";
// import VIcon from 'vue-awesome/components/Icon'

//import BlocklyJS from 'blockly/javascript';
import blocklyPython from "blockly/python";
import Blockly from "blockly";
//import Blockly from 'node-blockly/browser';
//import blocklyPython from 'node-blockly/python';

var axiosInstance = axios.create({
    baseURL: `${location.protocol}//${location.hostname}:3000`,
});

var axios_options = {
    proxy: {
        host: "127.0.0.1",
        port: 3000,
    },
};

export default {
    name: "Main",
    components: {
        Anotate,
        AnnotateForClassify,
        Capture,
        Train,
        TrainLocal,
        // eslint-disable-next-line vue/no-unused-components
        BlocklyComponent,
        // VIcon,
    },
    data: function () {
        return {
            hasImage: true,
            finishAnnotation: true,
            selectMode: "single",
            selectedMenu: 1,
            activetab: 1,
            nameState: null,
            projectDirIn: "",
            projectsName: [],
            projectsfromUSB: [],
            directorySelected: null,
            deletingProject: null,
            loaded: false,
            blockly_woakspace: null,
            code: "",
            code_file: "",
            options: {},
            isRunHiden: true,
            isStopHidden: false,
            isProjectLoaded: true,
            isRunning: false,
            //url: "http://192.168.88.243:8080/stream?topic=/output/image_detected&type=ros_compressed"
            url: "",
            ipAddress: "192.168.88.247",
            value: 0,
            max: 24,
            cmdVel: null,
            isSaving: false,
            isLoading: false,
            rbServer: null,
        };
    },
    methods: {
        rowSelected(items) {
            //console.log(items)
            return (this.selected = items);
        },
        rowClicked: function (item, index) {
            this.$store.dispatch(
                "changeProjectDir",
                this.projectsName[index].Projects
            );
            this.$store.dispatch("reqImages");            
        },
        rowDeleteSelected(items) {
            //console.log(items)
            this.selected = items;
            this.isProjectLoaded = true;
        },
        rowDeleteClicked: function (item, index) {
            this.$store.dispatch(
                "changeProjectDir",
                this.projectsName[index].Projects
            );
            this.deletingProject = this.projectsName[index].Projects;
        },
        handleProjectDelete: function (bvModalEvt) {
            if (this.deletingProject === null) {
                bvModalEvt.preventDefault();
            } else {
                this.$store.dispatch("deleteProject", this.deletingProject);
                this.$store.dispatch("regProjects").then(
                    () => {
                        console.log(
                            "Got some data, now lets show something in this component"
                        );
                        this.deletingProject = null;
                    },
                    () => {
                        console.error(
                            "Got nothing from server. Prompt user to check internet connection and try again"
                        );
                    }
                );
            }
        },
        deleteProject: function () {
            this.getAllProjects();
        },
        getAllProjects: function () {
            this.$store.dispatch("regProjects").then(
                () => {
                    console.log(
                        "Got some data, now lets show something in this component"
                    );
                    var projectNames = this.$store.getters.getProjects;
                    while (this.projectsName.length) {
                        this.projectsName.pop();
                        this.selectedMenu = 1;
                    }
                    projectNames.forEach(
                        function (item) {
                            this.projectsName.push({
                                Projects: item,
                            });
                        }.bind(this)
                    );
                    //this.projectsName = this.$store.getters.getProjects
                    //this.$store.dispatch('regProjects')
                    console.log(this.projectsName);
                },
                () => {
                    console.error(
                        "Got nothing from server. Prompt user to check internet connection and try again"
                    );
                }
            );
        },
        async listDirectoriesFromUSB() {
            const res = await axiosInstance.get("/getDirectories");
            if (res) {
                if (res.data.status === "error") {
                    this.$bvToast.toast(res.data.message, {
                        title: "Error!",
                        autoHideDelay: 3000,
                    });
                } else if (res.data.status === "success") {
                    this.projectsfromUSB = res.data.data.map((e) => ({
                        Project: e,
                    }));
                }
            }
        },
        onSelectDirectory(items) {
            if (items && items.length > 0) {
                this.directorySelected = items[0]["Project"];
            }
        },
        async loadFromUSB() {
            if (this.directorySelected) {
                const res = await axiosInstance.post("/loadFromUSB", {
                    projectName: this.directorySelected,
                });
                if (res) {
                    if (res.data.status === "error") {
                        this.$bvToast.toast(res.data.message, {
                            title: "Error!",
                            autoHideDelay: 3000,
                        });
                    } else if (res.data.status === "success") {
                        this.$bvToast.toast(res.data.message, {
                            title: "Success!",
                            autoHideDelay: 3000,
                        });
                        this.$store.dispatch("changeProjectDir", this.directorySelected);
                        this.$store.dispatch("reqImages");
                        this.loadWorkspace();
                        this.directorySelected = null;
                    }
                }
            }
        },
        async loadAllFromUSB() {
            this.isLoading = true;
            const res = await axiosInstance.post("/loadAllFromUSB");
            this.isLoading = false;
            if (res) {
                if (res.data.status === "error") {
                    this.$bvToast.toast(res.data.message, {
                        title: "Error!",
                        autoHideDelay: 3000,
                    });
                } else if (res.data.status === "success") {
                    this.$bvToast.toast(res.data.message, {
                        title: "Success!",
                        autoHideDelay: 3000,
                    });
                }
            }
        },
        async saveToUSB() {
            if (this.getProjectDir) {
                this.isSaving = true;
                const res = await axiosInstance.post("/saveToUSB", {
                    projectName: this.getProjectDir,
                });
                this.isSaving = false;
                if (res) {
                    if (res.data.status === "error") {
                        this.$bvToast.toast(res.data.message, {
                            title: "Error!",
                            autoHideDelay: 3000,
                        });
                    } else if (res.data.status === "success") {
                        this.$bvToast.toast(res.data.message, {
                            title: "Success!",
                            autoHideDelay: 3000,
                        });
                    }
                }

                var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace)
                let domToPretty = Blockly.Xml.domToPrettyText(xml)
                axiosInstance
                    .post('saveXML', {
                        filename: this.$store.getters.getProjectDir + '/test1.xml',
                        data: domToPretty,
                    })
                    .then((response) => {
                        console.log(response.data)
                        //this.isProjectLoaded = true
                    })
            }
        },
        async ejectUSB() {
            const res = await axiosInstance.post("/ejectUSB");
            if (res) {
                this.$bvToast.toast(res.data.message, {
                    title: "Success!",
                    autoHideDelay: 3000,
                });
            }
        },
        checkFormValidity() {
            const valid = this.$refs.form.checkValidity();
            this.nameState = valid ? "valid" : "invalid";
            return valid;
        },
        resetModal() {
            this.projectDirIn = "";
            this.nameState = null;
        },
        handleOk(bvModalEvt) {
            // Prevent modal from closing
            bvModalEvt.preventDefault();
            // Trigger submit handler
            this.handleSubmit();
        },
        handleSelect(type) {
            this.$store.dispatch("setTrainingType", type);
        },
        handleSubmit() {
            // Exit when the form isn't valid
            if (!this.checkFormValidity()) {
                return;
            }
            // Push the name to submitted names
            //this.submittedNames.push(this.projectDirIn)
            this.$store.dispatch("setProjectDir", this.projectDirIn);
            // Hide the modal manually
            this.$nextTick(() => {
                this.$store.dispatch("regProjects");
                this.$refs.modal.hide();
            });
            this.$store.dispatch("clearBlocklyWorkspace");
        },
        openProject(bvModalEvt) {
            // Prevent modal from closing
            bvModalEvt.preventDefault();
            // Trigger submit handler
            this.selectedProjectType();
        },
        selectedProjectType() {
            if (
                this.$store.getters.getTrainingType !== "None" &&
                this.getProjectDir !== "None"
            ) {
                this.$nextTick(() => {
                    this.$refs.openModal.hide();
                    this.loadWorkspace();
                    this.isProjectLoaded = false;
                });
            } else {
                console.log("Training type is required.");
            }
        },
        resetOpenModal() {
            this.$store.getTrainingType === "None";
        },
        handleTabChange(tabIndex) {
            console.log("Tabindex = " + tabIndex);
            // Because without using v-tab, Then index start with 1
            if (tabIndex == 1 && this.loaded == false) {
                this.isRunHiden = false;
            }
            if (tabIndex == 1) {
                this.isRunHiden = true;
            } else {
                this.isRunHiden = false;
            }

            if (tabIndex == 3) {

                if (this.$store.getters.getTrainingType === 'Image classification') {

                    console.log("get all files Image classification" + this.$store.state.projectDir);
                    axiosInstance.post("/getFiles", {
                        path: this.$store.state.projectDir
                    }).then((response) => {
                        console.log(response.data.files);
                        while (this.$refs.anotateForClassifyComponent.images.length) {
                            this.$refs.anotateForClassifyComponent.images.pop();
                        }
                        var info = response.data.files
                        var index, len
                        for (index = 0, len = info.length; index < len; ++index) {
                            var imPath =
                                response.data.projectDir +
                                response.data.folder +
                                '/' +
                                info[index].file
                            this.$refs.anotateForClassifyComponent.images.push({
                                fileName: info[index].file,
                                file: imPath,
                                id: info[index].id,
                                isAnnotated: info[index].isAnotated,
                                class: info[index].class,
                            })
                        }

                    });

                    axiosInstance.post("/getAnotaions", {
                        projectpath: this.$store.state.projectDir
                    }).then((response) => {
                        console.log(response.data.classes);
                        while (this.$refs.anotateForClassifyComponent.classes.length) {
                            this.$refs.anotateForClassifyComponent.classes.pop();
                        }

                        var info1 = response.data.classes
                        var index1, len1
                        for (index1 = 0, len1 = info1.length; index1 < len1; ++index1) {

                            this.$refs.anotateForClassifyComponent.classes.push({
                                Label: info1[index1]
                            })
                        }

                        console.log(this.$refs.anotateForClassifyComponent.classes)

                    });
                } else {
                    console.log("get all files Object deetection" + this.$store.state.projectDir);
                    axiosInstance.post("/getFiles", {
                        path: this.$store.state.projectDir
                    }).then((response) => {
                        console.log(response.data.files);
                        while (this.$refs.anotateComponent.images.length) {
                            this.$refs.anotateComponent.images.pop();
                        }
                        var info = response.data.files
                        var index, len
                        console.log(info.length)
                        for (index = 0, len = info.length; index < len; ++index) {
                            var imPath =
                                response.data.projectDir +
                                response.data.folder +
                                '/' +
                                info[index].file
                            this.$refs.anotateComponent.images.push({
                                fileName: info[index].file,
                                file: imPath,
                                id: info[index].id,
                                isAnnotated: info[index].isAnotated,
                                class: info[index].class,
                                classCounts: info[index].classCounts,
                            })
                            console.log(info[index].file)
                        }

                    });

                    axiosInstance.post("/getAnotaions", {
                        projectpath: this.$store.state.projectDir
                    }).then((response) => {
                        console.log(response.data.classes);
                        while (this.$refs.anotateComponent.classes.length) {
                            this.$refs.anotateComponent.classes.pop();
                        }

                        var info1 = response.data.classes
                        var index1, len1
                        for (index1 = 0, len1 = info1.length; index1 < len1; ++index1) {

                            this.$refs.anotateComponent.classes.push({
                                Label: info1[index1]
                            })
                        }

                        console.log(this.$refs.anotateComponent.classes)

                    });
                }

            }

            if (tabIndex == 2) {
                axiosInstance.post("/getFiles", {
                    path: this.$store.state.projectDir
                }).then((response) => {
                    console.log(response.data.files);
                    while (this.$refs.captureComponent.images.length) {
                        this.$refs.captureComponent.images.pop();
                    }
                    var info = response.data.files
                    var index, len
                    for (index = 0, len = info.length; index < len; ++index) {
                        var imPath =
                            response.data.projectDir +
                            response.data.folder +
                            '/' +
                            info[index].file
                        this.$refs.captureComponent.images.push({
                            fileName: info[index].file,
                            file: imPath,
                            id: info[index].id,
                        })
                    }

                });

            }

            if (tabIndex == 4) {

                this.$refs.trainLocalComponent.result = ""
                if (this.$store.getters.getTrainingType === 'Image classification') {
                    axiosInstance.post("/createImclassDataset", {
                        path: this.$store.state.projectDir
                    }).then((response) => {
                        console.log(response.data);

                    });
                } else {

                }
            }
        },

        showCode() {
            console.log("Hello world code!!!!! b4");
            this.code = blocklyPython.workspaceToCode(this.blockly_woakspace);
            //blocklyPython.workspaceToCode(this.blockly_woakspace).then((returnVal) => {
            //    console.log(returnVal.data.data)
            //})
            this.$refs.blocklyComponent.result = ""
            console.log("Hello world code!!!!!");
            this.isRunning = true;
            axiosInstance
                .post("run", {
                    filename: this.$store.getters.getProjectDir + "/test1.py",
                    data: this.code,
                })
                .then((response) => {
                    console.log(response.data);
                    this.isProjectLoaded = true;
                    //this.url = "http://192.168.88.243:8080/stream?topic=/output/image_detected&type=ros_compressed"
                    this.$refs["pyhonLoading"].show();
                    /* setTimeout(() => {

                                         this.url = "http://" + this.ipAddress + ":8080/stream?topic=/output/image_detected&type=ros_compressed"
                                         //this.url = "http://0.0.0.0:8080/stream?topic=/output/image_detected&type=ros_compressed"
                                         this.$refs.displayImage.src = this.url
                                         this.$refs['pyhonLoading'].hide()
                                         console.log(this.url)
                                     }, 12000)*/

                    var timerId, percent;
                    percent = 0;
                    timerId = setInterval(() => {
                        // increment progress bar
                        percent += 1;
                        console.log(percent);
                        this.value = percent;

                        // complete
                        if (percent >= 24) {
                            clearInterval(timerId);

                            this.$refs["pyhonLoading"].hide();
                        }
                    }, 500);
                    //this.url = "https://picsum.photos/250/250/?image=59"
                });
            console.log(this.code);
        },

        stopRun() {
            axiosInstance
                .post("stop", {
                    filename: this.$store.getters.getProjectDir + "/test1.py",
                    data: this.code,
                })
                .then((response) => {
                    console.log(response.data);
                    this.isProjectLoaded = false;
                    this.isRunning = false;
                });
        },
        saveWorkspace() {
            var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
            let domToPretty = Blockly.Xml.domToPrettyText(xml);
            axiosInstance
                .post("saveXML", {
                    filename: this.$store.getters.getProjectDir + "/test1.xml",
                    data: domToPretty,
                })
                .then((response) => {
                    console.log(response.data);
                    //this.isProjectLoaded = true
                });
            console.log(xml);
        },
        loadWorkspace() {
            console.log(this.$store.getters.getProjectDir + "/test1.xml");
            this.$store.dispatch("clearBlocklyWorkspace");

            axiosInstance
                .post("getXML", {
                    filename: this.$store.getters.getProjectDir + "/test1.xml",
                })
                .then((response) => {
                    console.log(response);
                    /*var xml = Blockly.Xml.textToDom(response.data)
                          console.log(xml)
                          Blockly.mainWorkspace.clear();
                          Blockly.Xml.domToWorkspace(Blockly.workspace, xml)*/

                    this.$store.commit("setBlocklyXml", response.data);

                    //Blockly.mainWorkspace.clear();

                    //let textToDom = Blockly.Xml.textToDom(response.data);
                    //Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, textToDom);

                    //console.log(xml)
                    //this.isProjectLoaded = true
                });
        },
        // linkProperties(route) {
        //   const routeName = route.name ? route.name : route
        //   const externalRoute = this.externalRoutes.filter(
        //     (r) => r.name === routeName,
        //   )[0]
        //   let url = externalRoute ? externalRoute.url : routeName

        //   if (externalRoute || url.match(/^(http(s)?|ftp):\/\//)) {
        //     if (route.query) {
        //       url = `${url}?${$.param(route.query)}`
        //     }

        //     return {
        //       is: 'a',
        //       href: url,
        //     }
        //   }

        //   return {
        //     is: 'router-link',
        //     to: {
        //       name: url,
        //       query: route.query,
        //     },
        //   }
        // },

        onForward: function () {
            // var x = 0
            var y = 0;
            var z = 0;
            var pub = true;
            if (pub === true) {
                // eslint-disable-next-line no-undef
                var twist = new ROSLIB.Message({
                    angular: {
                        x: 0,
                        y: 0,
                        z: z,
                    },
                    linear: {
                        x: 0.1,
                        y: y,
                        z: z,
                    },
                });
                console.log(twist);

                this.$store.getters.getCmdVel.publish(twist);
                //console.log(this.cmdVel);
            }
        },

        onBackward: function () {
            // var x = 0
            var y = 0;
            var z = 0;
            var pub = true;
            if (pub === true) {
                // eslint-disable-next-line no-undef
                var twist = new ROSLIB.Message({
                    angular: {
                        x: 0,
                        y: 0,
                        z: z,
                    },
                    linear: {
                        x: -0.1,
                        y: y,
                        z: z,
                    },
                });
                console.log(twist);

                this.$store.getters.getCmdVel.publish(twist);
                //console.log(this.cmdVel);
            }
        },
        onLeft: function () {
            // var x = 0
            var y = 0;
            var z = 0;
            var pub = true;
            if (pub === true) {
                // eslint-disable-next-line no-undef
                var twist = new ROSLIB.Message({
                    angular: {
                        x: 0,
                        y: 0,
                        z: -0.3,
                    },
                    linear: {
                        x: 0.1,
                        y: y,
                        z: z,
                    },
                });
                console.log(twist);

                this.$store.getters.getCmdVel.publish(twist);
                //console.log(this.cmdVel);
            }
        },

        onRight: function () {
            // var x = 0
            var y = 0;
            var z = 0;
            var pub = true;
            if (pub === true) {
                // eslint-disable-next-line no-undef
                var twist = new ROSLIB.Message({
                    angular: {
                        x: 0,
                        y: 0,
                        z: 0.3,
                    },
                    linear: {
                        x: 0.1,
                        y: y,
                        z: z,
                    },
                });
                console.log(twist);

                this.$store.getters.getCmdVel.publish(twist);
                //console.log(this.cmdVel);
            }
        },
        onCCW: function () {
            // var x = 0
            var y = 0;
            var z = 0;
            var pub = true;
            if (pub === true) {
                // eslint-disable-next-line no-undef
                var twist = new ROSLIB.Message({
                    angular: {
                        x: 0,
                        y: 0,
                        z: 0.3,
                    },
                    linear: {
                        x: 0,
                        y: y,
                        z: z,
                    },
                });
                console.log(twist);

                this.$store.getters.getCmdVel.publish(twist);
                //console.log(this.cmdVel);
            }
        },

        onCW: function () {
            // var x = 0
            var y = 0;
            var z = 0;
            var pub = true;
            if (pub === true) {
                // eslint-disable-next-line no-undef
                var twist = new ROSLIB.Message({
                    angular: {
                        x: 0,
                        y: 0,
                        z: -0.3,
                    },
                    linear: {
                        x: 0,
                        y: y,
                        z: z,
                    },
                });
                console.log(twist);

                this.$store.getters.getCmdVel.publish(twist);
                //console.log(this.cmdVel);
            }
        },

        getBlock() {},
    },
    mounted() {
        this.$store.dispatch("regProjects");

        //this.renderBlockly()

        this.cmdVel = this.$store.getters.getCmdVel;

        let uri = "getIP";
        console.log("Start roslibjs");
        // eslint-disable-next-line no-undef
        this.rbServer = new ROSLIB.Ros();
        this.rbServer.on("error", function (error) {
            this.connected = "Connection error" + error;
            console.log("Connection error");
        });

        this.rbServer.on(
            "close",
            function () {
                this.connected = "Disconnected event";
                console.log("Connection closed");
            }.bind(this)
        );

        this.rbServer.on(
            "connection",
            function () {
                console.log("Connected to ROS");
                this.connected = "Connected";

                // eslint-disable-next-line no-undef
                this.cmdVel = new ROSLIB.Topic({
                    ros: this.rbServer,
                    name: "/cmd_vel",
                    messageType: "geometry_msgs/Twist",
                });

                this.cmdVel.subscribe(
                    function (message) {
                        console.log("Received message on " + ": " + message.data);
                    }.bind(this)
                );

                this.$store.dispatch("setCmdVel", this.cmdVel);

                this.$store.commit('setRbServer', this.rbServer)

                let std_out_topic = new ROSLIB.Topic({
                    ros: this.rbServer,
                    name: "/std_out",
                    messageType: "std_msgs/String",
                });

                std_out_topic.subscribe(
                    function (message) {
                        console.log("Received message on " + ": " + message.data);
                        if (message.data === 'DONE') {
                            this.isRunning = false;
                            this.isProjectLoaded = false;

                        }
                        this.$refs.trainLocalComponent.result += message.data + '<br />'
                    }.bind(this)
                );

                let std_out_python_topic = new ROSLIB.Topic({
                    ros: this.rbServer,
                    name: "/std_out_python",
                    messageType: "std_msgs/String",
                });

                std_out_python_topic.subscribe(

                    function (message) {
                        var d = new Date()
                        var n = d.getTime()
                        console.log("Received message on " + ": " + message.data);
                        if (message.data === 'DONE') {
                            this.isProjectLoaded = false;
                            this.isRunning = false;

                        }
                        this.$refs.blocklyComponent.s_result = n + ": " + message.data + '<br />'
                    }.bind(this)
                );
            }.bind(this)
        );

        axiosInstance.get(uri, axios_options).then((response) => {

            this.rbServer.connect("ws://" + response.data.IP + ":9090");
            console.log("ROS IP = " + response.data.IP);
        });

    },
    computed: {
        ...mapGetters([
            "getProjectDir",
            "getProjects",
            "getImages",
            "getProjectStatus",
            "getCmdVel",
            "getTrainingType",
            "getBlocklyWorkspace",
        ]),
        getImgSrc: function () {
            return this.url;
        },
        saveButton: function () {
            return this.isSaving ? "Saving..." : "Save to usb";
        },

        /*
                getImgSrc: function () {
                    return this.imgSrc
                }*/
    },
    props: {
        msg: String,
    },
};
</script>

<style lang="scss" scoped>
$primary-color: #007e4e;
$black: #333;
$yellow: #fff7d6;
$grey: #eeeeee;

* {
    margin: 0;
    padding: 0;
    outline: none;
    box-sizing: border-box;
}

.p-color {
    color: $primary-color;
    font-weight: 800;
}

ul {
    list-style: none;
    padding: 0;
}

.op-btn {
    transition: opacity 0.3s ease-in;
    cursor: pointer;

    &:hover {
        opacity: 0.7;
    }
}

.container-fluid {
    padding: 0;
}

.main-bg {
    background-color: #eeeeee;
}

.content-panel {
    overflow-y: auto;
}

.left-panel {
    padding: 8px;
    max-width: 320px;
    width: 320px;
    min-width: 320px;
    overflow-y: auto;

    .l-title {
        color: #06754b;
        font-size: 35px;
        text-align: center;
    }

    .left-bottom-content {
        position: relative;
        background-color: #fff7d6;
        border-top-left-radius: 24px;
        border-top-right-radius: 24px;
        margin: 16px 8px;
        flex-direction: column;
        align-items: flex-start;
        padding: 20px 20px 0;
        height: 50%;
        overflow: hidden;

        .proj-name {
            display: flex;
            align-items: center;
            margin-bottom: 0px;

            svg {
                width: 25px;
                margin-right: 10px;
            }
        }

        .step {
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 15px;
            width: 100%;

            li {
                flex: 1 0 50%;
                padding: 5px;
                opacity: 1;
                filter: sepia(1);
                cursor: pointer;
                transition: opacity 0.3s ease-in, filter 0.3s ease-in;

                &.inactive {
                    opacity: 0.7;
                    filter: sepia(1) !important;
                    cursor: unset !important;
                }

                &.current {
                    filter: sepia(0) !important;
                }

                &:hover {
                    filter: sepia(0.5);
                }

                img {
                    width: 100%;
                }
            }
        }

        .hint {
            width: 100%;
            text-align: left;
            height: 53%;
            display: flex;
            justify-content: space-between;
            flex-direction: column;

            // overflow-y: scroll;
            .main-hint {
                overflow-y: scroll;
                height: calc(100% - 151px);
                padding: 0 5px;

                &.notype {
                    height: 100%;
                    margin-top: 20px;
                }
            }

            .btn-desc {
                margin-bottom: 10px;

                li {
                    display: flex;
                    align-items: center;
                    margin-bottom: 5px;
                    height: 23px;
                    margin-left: -7px;
                }

                span {
                    width: 32px;
                    display: flex;
                    justify-content: center;
                    margin-right: 5px;
                }
            }

            p {
                font-size: 0.8rem;

                img {
                    height: 30px;
                }
            }
        }

        .mascot {
            width: 100%;
            position: absolute;
            bottom: 0;
            left: 0;
            text-align: center;
        }
    }

    .menu-starter {
        >div {
            margin: 5px;
        }
    }

    .btn-base {
        width: 64px;
        height: 64px;
        background-position: center center;
        background-size: cover;
        cursor: pointer;

        &:hover {}

        &.new {
            background-image: url("../assets/UI/png/Group 105.png");
        }

        &.open {
            background-image: url("../assets/UI/png/Group 106.png");
        }

        &.save {
            background-image: url("../assets/UI/png/Group 107.png");
        }

        &.eject {
            background-image: url("../assets/UI/png/Group 108.png");
        }
    }
}

.sub-panel {
    background-color: #333333;
    padding: 16px;
    color: white;
    width: 240px;
    max-width: 240px;
}

.container {
    max-width: 100%;
    min-width: 100%;
    max-height: 100%;
    min-height: 100%;
    margin: 0px auto;
    font-size: 0.9em;
    color: #888;
}

#blocklyDiv {
    position: absolute;
    height: 100%;
    width: 100%;
    margin-left: 33.33%;
}

[data-md-tooltip] {
    position: relative;
}

[data-md-tooltip]:before {
    content: attr(data-md-tooltip);
    position: absolute;
    top: -35px;
    left: 50%;
    padding: 8px;
    transform: translateX(-50%) scale(0);
    transition: transform 0.2s ease-in-out;
    transform-origin: top;
    background-color: #fff7d6;
    color: #333;
    border-radius: 20px;
    font-size: 0.7rem;
    font-weight: 400;
    z-index: 9999;
    width: 120%;
    opacity: 1 !important;
    text-align: center;
}

[data-md-tooltip]:hover:before {
    transform: translateX(-50%) scale(1);
    z-index: 9999;
}
</style>
<style lang="scss">
.mode-select {
    .btn {
        color: unset;
        border: unset;
        background-color: unset;
        text-align: left;
        position: relative;

        &::after {
            position: absolute;
            top: 17px;
            right: 15px;
        }
    }
}

::-webkit-scrollbar {
    width: 7px;
    height: 10px;
}

::-webkit-scrollbar-thumb {
    // background-color: rgba(0, 0, 0, 0.2);
    background-color: #007e4e;
    border-radius: 10px;
}

::-webkit-scrollbar-track {
    background-color: rgba(0, 0, 0, 0.2);
    border-radius: 10px;
}

.mode-select {
    margin: 0;
    margin-bottom: 10px;
    width: 100%;
    background: #fff;
    border: 1px solid #ced4da;
    border-radius: .25rem;

    .btn {
        background-color: #fff;
    }
}
</style>
