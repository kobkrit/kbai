<template>
<div style="height: 100vh; width: 100vw;">
    <div class="train-panel">
        <button class="btn base-btn" :disabled="trainable" @click="onTrainLoc()">
            <b-spinner v-if="loading" small type="grow"></b-spinner>
            {{ isTraining ? "Training" : "Train" }}
        </button>
        <!-- <button class="btn base-btn" :disabled="!downloadable" @click="download">
            <b-spinner v-if="isDownloading" small type="grow"></b-spinner>
            Download
        </button> -->
    </div>
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
import {
    mapGetters
} from "vuex";

var axios_options = {
    proxy: {
        host: "127.0.0.1",
        port: 3000,
    },
};

axios.defaults.timeout = 300000;

var trainInstance = axios.create({
    baseURL: `${location.protocol}//${location.hostname}:8080`,
});

var apiInstance = axios.create({
    baseURL: `${location.protocol}//${location.hostname}:3000`,
});

var axiosInstance = axios.create({
    baseURL: `${location.protocol}//${location.hostname}:3000`,
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
            std_out_topic: undefined,
            std_out_message: "",
        };
    },
    methods: {
        prepareData: function () {
            this.result += `Preparing data ... <br />`;
            return apiInstance.get(`/archiveForClassify/${this.getProjectDir}`, {
                responseType: "arraybuffer",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/zip",
                },
            });
        },
        checkRunning: function () {
            return trainInstance.get(`/train/is_running`);
        },
        stopTraining: function () {
            return trainInstance.get(`/train/stop`);
        },
        getLogs: function () {
            return trainInstance.get(`/train/log`);
        },
        download: async function () {
            this.isDownloading = true;
            try {
                const res = await apiInstance.post(`/downloadClassifier`, {
                    projectName: this.getProjectDir,
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
                    }
                }
            } catch (e) {
                console.log(e);
            }
            this.isDownloading = false;
        },
        onTrainLoc: async function () {
            apiInstance.post("/retrainImg", {
                projectpath: this.$store.getters.getProjectDir
            }).then(function (response) {
                console.log(response.data);
            })
        },
        onTrain: async function () {
            this.loading = true;
            this.isDone = false;
            this.isTraining = false;
            this.result = "";
            this.logs = "";
            try {
                const data = await this.prepareData();
                this.result += `Successfully prepare data. <br />`;
                let formData = new FormData();
                var file = new File([data.data], "images.zip", {
                    type: "application/zip",
                });
                formData.append("file", file);
                let vm = this;
                trainInstance
                    .post(`/upload`, formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        },
                    })
                    .then(function (res) {
                        vm.result += `${res.data} <br />`;
                        vm.isTraining = true;
                        const polling = setInterval(async () => {
                            const res = await vm.checkRunning();
                            const log = await vm.getLogs();
                            vm.logs = log.data
                                .replace(/(?:\r\n|\r|\n)/g, "<br>")
                                .replace(/\d+/gm, "");
                            if (res.data === "False") {
                                vm.loading = false;
                                vm.isDone = true;
                                clearInterval(polling);
                            }
                        }, 3000);
                    })
                    .catch(function (e) {
                        console.error(e);
                        vm.result += `failed to upload data. <br />`;
                        vm.loading = false;
                    });
            } catch (e) {
                if (e.response.status === 404) {
                    this.$bvToast.toast("Cannot get classification labels!", {
                        title: "Error!",
                        autoHideDelay: 3000,
                    });
                } else {
                    this.$bvToast.toast("Something went wrong!", {
                        title: "Error!",
                        autoHideDelay: 3000,
                    });
                }
                this.loading = false;
                this.isTraining = false;
                console.log(e);
            }
        },
    },
    directives: {},
    mounted() {
        //console.log(this.rbServer)

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
        trainable: function () {
            return this.loading;
        },
        variantType: function () {
            return this.isTraining ? "primary" : "outline-primary";
        },
        downloadable: function () {
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
    display: flex;
    justify-content: flex-end;
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
    height: calc(100vh - 78px);
    overflow-y: scroll;
    text-align: left;
    padding: 20px !important;
    background-color: #333 !important;
}
</style>
