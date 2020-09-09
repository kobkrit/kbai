<template>
<div class="w-100 h-100">
    <div class="d-flex w-100 h-100 outer-wrap">
        <div class="d-flex flex-fill flex-column main-panel" style="background-color:white;">
            <div class="d-flex flex-fill align-items-center justify-content-center">
                <div class="row">
                    <b-col md="auto">
                        <div class="image-container">
                            <!--<b-img crossorigin="anonymous" ref="displayImage" style="margin-top: 10px; width: 100%;" :src="getImgSrc" alt="Center image"></b-img>-->
                            <!-- <video id="webcam" autoplay playsinline width="640" height="480"></video>
                            <canvas id="canvas" class="d-none"></canvas> -->
                            <Camera ref="camera" width="640" height="480" />
                            <!-- <audio id="snapSound" src="audio/snap.wav" preload="auto"></audio> -->
                        </div>
                    </b-col>
                </div>
            </div>
            <div class="img-slider">
                <!-- <VueSlickCarousel v-if="images.length" v-bind="settings" class="carouselContainer">
                    <div v-for="file in images" :key="file.id">
                        <div class="img"><img :src="file.file" alt="" srcset=""></div>
                    </div>
                </VueSlickCarousel> -->

                <!-- <div class="img active"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div>
                <div class="img"><img class="thumb" src="../assets/UI/png/Group 116.png" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" alt="" srcset=""></div> -->

                <div :id="id" :class="{'img': true, 'active': imageActiveIndex === id }" v-for="(file, id) in images" :key="id" v-on:click="onSelect($event)">
                    <img class="thumb" :src="file.file" alt="" srcset=""><img class="cancel-btn" src="../assets/UI/png/cancel.png" @click="deleteImage(id)" alt="" srcset="">
                </div>
            </div>
        </div>
        <div class="side-panel" style="width:300px;">
            <div class="center">
                <img @click="takePhoto" v-on:click.prevent class="camera-btn op-btn" src="../assets/UI/png/Group 116.png" height="128" alt="" srcset="" />
                <!-- <div class="next op-btn">
                    <span>ANNOTATE</span>
                    <span class="ico"><img src="../assets/UI/svg/up-arrow.svg" alt="" srcset="" /></span>
                </div> -->
            </div>
            <!-- <div class="display-panel">
                <p class="display-image">
                    <canvas
                        rcrossorigin="anonymous"
                        ref="myCanvas"
                    />
                </p>
             </div>-->
        </div>
    </div>
    <b-modal ref="capture-modal" hide-footer title="Using Component Methods">
        <div class="d-block text-center">
            <h3> New image has been captured!</h3>
        </div>
    </b-modal>
</div>
</template>

<script>
//import VueSlickCarousel from "vue-slick-carousel";
//import "vue-slick-carousel/dist/vue-slick-carousel.css";

// optional style for arrows & dots
//import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import axios from "axios";
//import LongPress from 'vue-directive-long-press'

//import VueAxios from 'vue-axios';
import "vue-awesome/icons";
// import Webcam from 'webcam-easy';
// import VIcon from "vue-awesome/components/Icon";
import {
    mapGetters
} from "vuex";

// var convert = require("xml-js");
import Camera from "vue-html5-camera"



var axios_options = {
    proxy: {
        host: "127.0.0.1",
        port: 3000,
    },
};

var axiosInstance = axios.create({
    baseURL: `${location.protocol}//${location.hostname}:3000`,
});

export default {
    name: "Capture",
    components: {
        /*VueSlickCarousel,*/
    },
    props: {},
    created() {},
    data() {
        return {
            /*settings: {
                dots: false,
                slidesToShow: 5,
                slidesToScroll: 1,
                infinite: false
            },*/
            ipAddress: "192.168.88.247",
            connected: "Disconnected",
            teleop: null,
            cmdVel: null,
            rbServer: null,
            imgSrc: null,
            projectDirIn: "",
            nameState: null,
            images: [],
            imageActiveIndex: undefined,
            showCapturing: false,
            src: ""
        };
    },
    methods: {
        doNothing: function () {},
        createProject: function () {
            this.$store.dispatch("setProjectDir", "myProject");
        },
        takePhoto: async function(){
            console.log("takePhoto");
            this.src = this.$refs.camera.click();
            console.log(this.src);
            await axiosInstance
                .post('/upload/image', {
                    path: this.$store.state.projectDir,
                    base64image: this.src,
                })
                .then((response) => {
                    console.log(response.data)
                    if (response.data.status === 'OK') {
                        console.log('File is OK!!!!')
                        this.showCapturing = false
                        this.$refs['capture-modal'].hide()

                        //this.$refs['saveAnotation'].show()
                        axiosInstance.post("/getFiles", {
                            path: this.$store.state.projectDir
                        }).then((response) => {
                            console.log(response.data.files);
                            while (this.images.length) {
                                this.images.pop();
                            }
                            var info = response.data.files
                            var index, len
                            for (index = 0, len = info.length; index < len; ++index) {
                                var imPath =
                                    '/' +
                                    info[index].file
                                this.images.push({
                                    fileName: info[index].file,
                                    file: imPath,
                                    id: info[index].id,
                                })
                            }

                        });
                        //return true;
                    }
                })
                .catch((error) => {
                    console.log(error)
                    //return false;
                }).this

            //return true
        },
        getImage: async function () {
            //var c = this.$refs.myCanvas;
            this.showCapturing = true
            this.$refs['capture-modal'].show()
            var c = document.createElement('canvas');
            c.width = 640;
            c.height = 480;
            var ctx = c.getContext("2d");
            var img = this.$refs.displayImage;
            //const img = new Image();
            //img.src = this.imgSrc
            //img.onload = () => {
            //    ctx.drawImage(img, 0, 0);
            //};
            ctx.drawImage(img, 0, 0);
            //imgData64 = c.toDataURL()
            //console.log(c.toDataURL());
            //this.$store.dispatch("uploadImage", c.toDataURL());

            await axiosInstance
                .post('/upload/image', {
                    path: this.$store.state.projectDir,
                    base64image: c.toDataURL(),
                })
                .then((response) => {
                    console.log(response.data)
                    if (response.data.status === 'OK') {
                        console.log('File is OK!!!!')
                        this.showCapturing = false
                        this.$refs['capture-modal'].hide()

                        //this.$refs['saveAnotation'].show()
                        axiosInstance.post("/getFiles", {
                            path: this.$store.state.projectDir
                        }).then((response) => {
                            console.log(response.data.files);
                            while (this.images.length) {
                                this.images.pop();
                            }
                            var info = response.data.files
                            var index, len
                            for (index = 0, len = info.length; index < len; ++index) {
                                var imPath =
                                    '/' +
                                    info[index].file
                                this.images.push({
                                    fileName: info[index].file,
                                    file: imPath,
                                    id: info[index].id,
                                })
                            }

                        });
                        //return true;
                    }
                })
                .catch((error) => {
                    console.log(error)
                    //return false;
                }).this

            //return true
        },
        deleteImage: function (index) {

            console.log("Image has been deleted");
            console.log(index)
            console.log(this.images[index].fileName)

            axiosInstance
                .post("deleteImage", {
                    projectpath: this.$store.getters.getProjectDir,
                    filename: this.images[index].fileName,

                })
                .then((response) => {
                    console.log(response.data);
                    axiosInstance.post("/getFiles", {
                        path: this.$store.state.projectDir
                    }).then((response) => {
                        console.log(response.data.files);
                        while (this.images.length) {
                            this.images.pop();
                        }
                        var info = response.data.files
                        var index, len
                        for (index = 0, len = info.length; index < len; ++index) {
                            var imPath =
                                '/' +
                                info[index].file
                            this.images.push({
                                fileName: info[index].file,
                                file: imPath,
                                id: info[index].id,
                            })
                        }

                    });
                });
        },
        onSelect: function (event) {
            console.log("pop array")
            var targetId = event.currentTarget.id
            console.log(targetId); // returns 'foo'
            var index = Number(targetId)
            this.imageActiveIndex = index

            // console.log(this.images[index].file)
            console.log(this.$store.getters.getImages[index].file);
            this.imSrc = this.$store.getters.getImages[index].file;
            this.selectedFile = this.$store.getters.getImages[index].fileName;
            this.imFolder = "images";

            return (this.selectedIndx = index);

        },
        onForward: function () {
            // var x = 0;
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

                this.cmdVel.publish(twist);
                console.log(this.cmdVel);
            }
        },
        onBackward: function () {
            // var x = 0;
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

                this.cmdVel.publish(twist);
                console.log(this.cmdVel);
            }
        },
        onLeft: function () {
            // var x = 0;
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

                this.cmdVel.publish(twist);
                console.log(this.cmdVel);
            }
        },
        onRight: function () {
            // var x = 0;
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

                this.cmdVel.publish(twist);
                console.log(this.cmdVel);
            }
        },
        onCCW: function () {
            // var x = 0;
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

                this.cmdVel.publish(twist);
                console.log(this.cmdVel);
            }
        },
        onCW: function () {
            // var x = 0;
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

                this.cmdVel.publish(twist);
                console.log(this.cmdVel);
            }
        },
    },

    directives: {},

    mounted() {

        axiosInstance.get("getIP", axios_options).then((response) => {
            this.ipAddress = response.data.IP;
            this.imgSrc =
                "http://" +
                this.ipAddress +
                ":8080/stream?topic=/output/image_raw&type=ros_compressed";

        });

        // const webcamElement = document.getElementById('webcam');
        // const canvasElement = document.getElementById('canvas');
        // const snapSoundElement = document.getElementById('snapSound');
        // const webcam = new Webcam(webcamElement, 'user', canvasElement, snapSoundElement);

        // webcam.start()
        //     .then(result => {
        //         console.log("webcam started");
        //     })
        //     .catch(err => {
        //         console.log(err);
        //     });

        console.log("Started roslibjs");
    },
    computed: {
        ...mapGetters(["getProjectDir"]),
        getImgSrc: function () {
            return this.imgSrc;
        },
        //getProjectDir() {
        //    return this.$store.state.projectDir
        //}
    },
    components:{
        Camera
    }
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

.side-panel {
    padding: 15px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
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

#logo .fa-icon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.btn-space {
    margin-right: 5px;
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
    position: relative;
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

    .cancel-btn {
        position: absolute;
        right: 10px;
        top: 10px;
        width: 30px;
        height: 30px;
    }
}

.display-panel {
    border-radius: 8px;
    background-color: #333;
    overflow: hidden;
    margin-top: 15px;

    .display-image {
        margin: 0;

        canvas {
            min-height: 180px;
            height: 180px;
            width: 100%;
            object-fit: cover;
        }
    }
}
</style>
