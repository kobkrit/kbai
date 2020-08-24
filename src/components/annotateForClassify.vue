<template>
<div class="w-100 h-100">
    <div class="d-flex w-100 h-100 outer-wrap">
        <div class="d-flex flex-fill flex-column main-panel" style="background-color:white;">
            <div class="d-flex flex-fill align-items-center justify-content-center">

                <div class="row">
                    <b-col md="auto">
                        <div class="image-container">
                            <p class="img"><img :src="imSrc" @load="loadCb" alt="" srcset=""></p>
                            <p v-if="images[imageActiveIndex] && images[imageActiveIndex].isAnnotated == 1">
                                {{images[imageActiveIndex].class}}
                            </p>
                        </div>
                    </b-col>
                </div>
            </div>
            <div class="img-slider">
                <!-- <VueSlickCarousel v-if="images.length" v-bind="settings" @beforeChange="onBeforeChange" class="carousel ">
                    <div :id="id" :class="{'item-slider': true, 'active': imageActiveIndex === id }" v-for="(file, id) in images" :key="id" v-on:click="onSelect($event)">
                        <img v-if="file.isAnnotated == 1" src="../assets/UI/png/cancel.png" class="cancel-btn op-btn" />
                        <div>
                            <p class="img"><img :src="file.file" alt="" srcset=""></p>
                        </div>
                    </div>
                </VueSlickCarousel> -->
                
                <!-- <div class="img active"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="annotated-btn" src="../assets/UI/png/tick.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="annotated-btn" src="../assets/UI/png/tick.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="annotated-btn" src="../assets/UI/png/tick.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="annotated-btn" src="../assets/UI/png/tick.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""></div> -->
                <div :id="id" :class="{'img': true, 'active': imageActiveIndex === id }" v-for="(file, id) in images" :key="id" v-on:click="onSelect($event)">
                    <img class="thumb" :src="file.file" alt="" srcset=""><img v-if="file.isAnnotated == 1" class="annotated-btn" src="../assets/UI/png/tick.png" alt="" srcset="">
                </div>
            </div>
        </div>

        <div class="side-panel">
            <div class="d-flex flex-fill w-100 flex-column align-items-start right-panel-cn">
                <h4 class="font-weight-bold">LABEL</h4>
                <button @click="onNewLabel" class="btn btn-light new-label w-100">
                    New label
                    <img src="../assets/UI/png/+.png" alt="" style="position: absolute;right: 15px;" srcset="" />
                </button>

                <!--<b-button class="mb-2" pill variant="primary" v-b-modal.anotateDiaglog>Add label</b-button>-->

                <div class="pills w-100 mt-2" v-for="(cls, index) in classes" :key="index">
                    <button type="button" @click="selectLabel(cls.Label)" class="btn added-label w-100">
                        {{cls.Label}}
                        <div style="position: absolute;right: 15px;" class="right-group">
                            <img src="../assets/UI/svg/interface.svg" height="26" alt="" class="interface-btn" srcset="" />
                            <img class="ml-2" src="../assets/UI/png/Group 114.png" @click.stop="deletetLabel(index)" height="22" alt="" srcset="" />
                        </div>
                    </button>

                </div>
                <h4 class="font-weight-bold mt-2">ANNOTATE</h4>

            </div>
            <div class="w-100">
                <!-- <div class="next op-btn" @click="onClick" v-on:click.prevent>
                    <span>TRAINING</span>
                    <span class="ico"><img src="../assets/UI/svg/up-arrow.svg" alt="" srcset=""></span>
                </div> -->
            </div>
        </div>
    </div>

    <b-modal ref="class-modal" id="anotateDiaglog" title="Add a label" hide-footer>
        <b-form @submit="onSubmit" @reset="onReset">
            <b-container fluid class="bv-example-row">
                <b-form-row class="mb-3">
                    <b-form-input id="input-2" v-model="form.name" required placeholder="Enter name"></b-form-input>
                </b-form-row>
                <b-form-row>
                    <b-col md="4">
                        <b-button pill block type="submit" variant="primary">Ok</b-button>
                    </b-col>
                    <b-col md="4" class="ml-md-auto ">
                        <b-button pill block type="reset" variant="danger">Reset</b-button>
                    </b-col>
                </b-form-row>
            </b-container>
        </b-form>
    </b-modal>
</div>
</template>

<script>
//import VueSlickCarousel from "vue-slick-carousel";
//import "vue-slick-carousel/dist/vue-slick-carousel.css";

// optional style for arrows & dots
//import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import {
    clipperBasic
} from "vuejs-clipper";
import {
    Multipane,
    MultipaneResizer
} from "vue-multipane";

//import Splitpanes from 'splitpanes'
//import 'splitpanes/dist/splitpanes.css'

import "vuejs-clipper/dist/vuejs-clipper.css";
import axios from "axios";
import {
    mapGetters
} from "vuex";

var convert = require("xml-js");
//const API_URL = "http://172.20.10.2:3000/getFiles";

var axiosInstance = axios.create({
    baseURL: `${location.protocol}//${location.hostname}:3000`,
});

export default {
    name: "Anotate",
    components: {
        clipperBasic,
        Multipane,
        MultipaneResizer,
        //VueSlickCarousel,

        //Splitpanes,
    },
    props: {},
    created() {},
    data() {
        return {
            imageActiveIndex: undefined,
            anotaionActiveIndex: undefined,
            /*settings: {
                dots: false,
                slidesToShow: 5,
                slidesToScroll: 1,
            },*/
            form: {
                name: "",
            },
            sortBy: "name",
            bndFields: [{
                    key: "name",
                    sortable: false,
                },
                {
                    key: "bndbox",
                    sortable: false,
                },
                {
                    key: "Actions",
                },
            ],
            imageFields: [{
                key: "file",
                sortable: false,
            }, ],
            fullPath: "",
            projectDir: "",
            imFolder: "",
            images: [],
            selectedFile: "",
            selectedPath: "",
            classes: [],
            classesFields: [{
                    key: "Label",
                },
                {
                    key: "actions",
                    label: "Actions",
                },
            ],
            modes: ["multi", "single", "range"],
            selectMode: "single",
            selected: [],
            im_file: "",
            selectedIndx: 3,
            imSrc: "./round_image_black_48dp.png",
            options: {},
            sel: {},
            anotate: {
                annotation: {
                    folder: " ",
                    filename: " ",
                    path: " ",
                    source: {
                        database: "Unknown",
                    },
                    size: {
                        width: 500,
                        height: 300,
                        depth: 3,
                    },
                    segmented: 0,
                    object: [],
                },
            },
            info: [],
            anotationWidth: 100,
            anotationHeight: 100,
            anotationX: 0,
            anotationY: 0,
            annotationName: "",
            showBound: false,
            savedXmlFilename: "",
            std_out_topic: undefined,
        };
    },
    methods: {

        selectLabel: async function (label) {
            console.log("Label = " + label);

            console.log("File name = " + this.selectedFile)

            await axiosInstance
                .post("/addClass", {
                    class: label,
                    file: this.selectedFile,
                    projectpath: this.$store.getters.getProjectDir

                })
                .then((response) => {
                    console.log(response.data);
                    if (response.data.status === "OK") {
                        console.log("File is OK!!!!");

                        console.log(response.data.files);

                        this.images[this.imageActiveIndex].isAnnotated = 1
                        this.images[this.imageActiveIndex].class = label

                    }
                })
                .catch((error) => {
                    console.log(error);
                });
            console.log("Done anotation!!!!!!");
        },

        onBeforeChange: async function (oldSlideIndex, newSlideIndex) {
            console.log("Before change")

        },
        onNewLabel: function () {
            this.$refs["class-modal"].show();
            console.log("New LABEL")
        },
        imageSrc: function () {
            console.log("Image sr called!!!!");
            console.log(this.images[this.selectedIndx].file); // this.images[this.selectedIndx].file)
            return this.images[this.selectedIndx].file; //this.images[this.selectedIndx].file
        },
        onSelect: function (event) {
            console.log("pop array")
            var targetId = event.currentTarget.id
            console.log(targetId); // returns 'foo'
            var index = Number(targetId)
            this.imageActiveIndex = index

            while (this.anotate.annotation.object.length) {
                this.anotate.annotation.object.pop();
            }

            this.showBound = false;
            console.log("Hello");
            console.log(event);
            //console.log(this.images[index].file)
            console.log(this.images[index].file);
            this.imSrc = this.images[index].file;
            this.selectedFile = this.images[index].fileName;
            this.imFolder = "images";

            return (this.selectedIndx = index);

        },
        onClick: function () {
            console.log("Click")
            //this.images = this.$store.getters.getImages;
            console.log(this.images)

        },
        rowSelected(items) {
            console.log(items);
            return (this.selected = items);
        },

        deleteBox: function (row) {
            this.anotate.annotation.object.pop(row);
        },
        delAnotateFunc: function () {
            this.anotate.annotation.object.pop();
        },
        loadCb: function () {
            var imsr = this.imageSrc();

            this.anotate.annotation.filename = this.selectedFile;
            this.anotate.annotation.folder = this.imFolder.substr(
                1,
                this.imFolder.length
            );
            this.anotate.annotation.path = this.fullPath + "/client/" + imsr; //imsr.substr(1, imsr.length);
            if (this.images === undefined || this.images.length == 0) {
                // array empty or does not exist
            } else {
                var img = new Image();
                img.src = this.imageSrc();

                img.onload = function () {
                    // here you got the width and height
                    this.anotate.annotation.size.width = img.width;
                    this.anotate.annotation.size.height = img.height;
                }.bind(this);

                img.onerror = function () {
                    console.log("Load image error");
                }.bind(this);
            }
        },
        onSubmit(evt) {
            evt.preventDefault();
            this.classes.push({
                Label: this.form.name,
            });

            axiosInstance
                .post("/imclassAnotaion", {
                    dirname: this.form.name,
                    projectpath: this.$store.getters.getProjectDir
                })
                .then((response) => {
                    console.log(response.data);
                    if (response.data.status === "OK") {
                        console.log("File is OK!!!!");

                       
                    } else {
                        console.log("File is FAIL!!!!");
                    }
                })
                .catch((error) => {
                    console.log(error);
                });

            console.log(this.classes);
            this.$refs["class-modal"].hide();
        },
        deletetLabel: function (index) {
            console.log(index)
            console.log(this.classes[index].Label)

            axiosInstance
                .post("/removeImclassAnotaion", {
                    dirname: this.classes[index].Label,
                    projectpath: this.$store.getters.getProjectDir
                })
                .then((response) => {
                    console.log(response.data);
                    if (response.data.status === "OK") {
                        console.log("File is OK!!!!");
                        this.classes.splice(index, 1);

                        
                    } else {
                        console.log("File is FAIL!!!!");
                    }
                })
                .catch((error) => {
                    console.log(error);
                });

        },
        onReset: function () {},

    },
    directives: {},
    mounted() {
        console.log("Anotation")
        this.images = this.$store.getters.getImages;
        console.log(this.images)
        this.projectDir = this.$store.getters.getProjectDir;


    },
    computed: {
        ...mapGetters(["getProjectDir", "getImages"]),
        drawBox() {
            var sty =
                "position: absolute;" +
                "top: 0;" +
                "left: 0;" +
                "width: " +
                this.anotationWidth +
                "px;" +
                "height: " +
                this.anotationHeight +
                "px;" +
                "margin-top: " +
                this.anotationY +
                "px;" +
                "margin-left: " +
                this.anotationX +
                "px;" +
                "display: none;" +
                "color: #FFF;" +
                "display: block;" +
                "background: rgba(0, 0, 0, .5);";
            console.log(sty);

            return sty;
        },

        getImagesData() {
            this.images = this.$store.getters.getImages;
            console.log(this.images)
            return this.images
        },
    },
};
</script>

<style lang="scss" scoped>
$primary-color: #007e4e;

.op-btn {
    transition: opacity 0.3s ease-in;
    cursor: pointer;

    &:hover {
        opacity: 0.7;
    }
}

.pills {
    max-height: 15%;
    overflow-y: scroll;
}

.annotate-cn-list {
    max-height: 65%;
    overflow-y: scroll;
}

.annotate-cn {
    text-align: left;
    padding: 8px;
    background-color: #ddd;
    border-radius: 8px;
    position: relative;
    margin-bottom: 10px;
    opacity: 0.7;
    border: 5px solid rgba($color: #000000, $alpha: 0);
    cursor: pointer;
    transition: opacity 0.3s ease-in;

    .annotation-txt {
        color: $primary-color;
    }

    &:last-child {
        margin-bottom: 0;
    }

    &.active {
        border: 5px solid $primary-color;
        opacity: 1;
    }

    &:hover {
        opacity: 1;
    }
}

.badge-icn {
    position: absolute;
    left: 10px;
    top: 10px;
    background-color: $primary-color;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
}

.cancel-btn {
    position: absolute;
    right: 5px;
    top: 5px;
    cursor: pointer;
}

.right-panel-cn {
    overflow-y: auto;
}

.interface-btn {
    &:hover {
        color: white;
    }
}

.right-group {
    position: absolute;
    right: 15px;
    top: 0;
    bottom: 0;
    display: flex;
    vertical-align: middle;
    align-items: center;
}

.badge {
    background-color: white;
    border-radius: 50%;
    width: 26px;
    height: 26px;
    padding: 2px;
}

.added-label {
    position: relative;
    border-radius: 16px;
    text-align: left;
    background-color: #dddddd;
    border: 1px solid #ddd;
    margin-bottom: 5px;

    &.active {
        background-color: $primary-color;
        color: white;
    }

    &:last-child {
        margin-bottom: 0;
    }
}

.new-label {
    position: relative;
    border-radius: 16px;
    text-align: left;
    color: $primary-color;
}

.side-panel {
    padding: 15px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    width: 300px;

    .next {
        height: 50px;
        background: #ffffff 0% 0% no-repeat padding-box;
        border-radius: 38px;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        margin-top: 15px;

        span {
            color: $primary-color;
            font-size: 1.5rem;
            font-weight: 800;

            &.ico {
                position: absolute;
                top: 7px;
                right: 18px;
            }
        }
    }
}

/*.slick-slider {
    width: 500px;
    flex: 1 1 auto;

    .cancel-btn {
        position: absolute;
        right: 10px;
        top: 10px;
        width: 30px;
        height: 30px;
    }

    .item-slider {
        position: relative;
        opacity: 0.7;
        transition: opacity 0.3s ease-in;
        cursor: pointer;

        &.active,
        &:hover {
            opacity: 1;
        }

        &.active::after {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            border: 5px solid $primary-color;
            border-radius: 25px;
            pointer-events: none;
        }
    }

    div {
        outline: none;
    }

    .img {
        background-color: #2f3241;
        height: 160px;
        margin: 3px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 20px;
        overflow: hidden;

        img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    }

    ::v-deep .slick-arrow:before {
        color: #2f3241;
        font-size: 33px;
        transition: opacity 0.3s ease-in;
    }

    ::v-deep .slick-prev {
        left: -40px;
    }
}*/

.my-clipper {
    width: 100%;
}

.custom-resizer {
    width: 100%;
    height: 100vh;
}

.custom-resizer>.pane {
    text-align: left;
    padding: 10px;
    overflow: hidden;
    background: #eee;
    border: 1px solid #ccc;
}

.custom-resizer>.multipane-resizer {
    margin: 0;
    left: 0;
    width: 8px;
    position: relative;
    background: #999;

    &:before {
        display: block;
        content: "";
        width: 3px;
        height: 100vh;
        position: absolute;
        top: 0%;
        left: 50%;
        margin-top: 0vh;
        margin-left: -1.5px;
        border-left: 1px solid #444;
        border-right: 1px solid #444;
    }

    &:hover {
        &:before {
            border-color: #999;
        }
    }
}

.container_middle {
    width: 100%;
    padding-right: 0px;
    padding-left: 0px;
    margin-right: 1px;
    margin-left: 1px;
}

.splitpanes {
    .splitpanes__pane {
        box-shadow: 0 0 3px rgba(185, 185, 185, 0.2) inset;
        justify-content: center;
        align-items: center;
        display: flex;
        position: relative;
    }
}

.splitpanes span {
    font-family: Helvetica, Arial, sans-serif;
    color: #f00;
    opacity: 0.7;
}

em.specs {
    font-size: 0.2em;
    line-height: 1;
    position: absolute;
    color: #999;
    bottom: 0.5em;
    left: 0;
    right: 0;
    text-align: center;
}

.multipane.foo.layout-v .multipane-resizer {
    margin: 0;
    left: 0;
    /* reset default styling */
    width: 10px;
    background: #999;
}

.vertical-panes {
    width: 100%;
    height: 100%;
    border: 1px solid #ccc;
}

.vertical-panes>.pane {
    text-align: left;
    padding: 15px;
    overflow: hidden;
    background: #eee;
}

html,
body {
    height: 100%;
}

.container-fluid {
    height: 100%;
    overflow-y: hidden;
    /* don't show content that exceeds my height */
}

.body-film {
    min-height: 100%;
    overflow-y: scroll;
}

.my-table {
    max-height: 600px;
    overflow-y: scroll;
}

.fullHeight {
    height: 100%;
    background: rebeccapurple;
}

.image-container {
    position: relative;
    width: 100%;
    height: 100%;
}

.image-container .after {
    position: absolute;
    top: 0;
    left: 0;
    width: 50px;
    height: 50px;
    margin-top: 30px;
    margin-left: 30px;
    display: none;
    color: #fff;
    display: block;
    background: rgba(121, 121, 121, 0.5);
}

.outer-wrap {
    overflow: hidden;
}
.main-panel {
    width: calc(100% - 300px);
}
.img-slider {
    display: -webkit-box;
    width: 100%;
    overflow-x: scroll;
    height: 180px;
    position:relative;
    padding-top: 6px;
    margin: 20px;

    .img {
        background-color: #2f3241;
        height: 160px;
        width: 160px;
        margin: 0 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 20px;
        overflow: hidden;
        position: relative;
        opacity: 0.7;
        transition: opacity 0.3s ease-in;
        cursor: pointer;

        &.active,
        &:hover {
            opacity: 1;
        }

        &.active::after {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            border: 7px solid $primary-color;
            border-radius: 20px;
            pointer-events: none;
        }

        .thumb {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    }
    .annotated-btn {
        position: absolute;
        right: 10px;
        top: 10px;
        width: 30px;
        height: 30px;
    }
}
</style>
