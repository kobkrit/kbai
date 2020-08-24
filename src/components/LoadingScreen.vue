<template>
  <div class="hello">
    <div class="panel">
      <div class="mascot">
        <img src="../assets/UI/png/Group 102.png" alt="" srcset="" />
        <div class="balloon">
          <p class="txt">
            ยินดีต้อนรับเข้าสู่ <span class="highlight">KidBright AI IDE</span
            ><br /><span class="name">น้องขนมชั้น</span
            >ทำหน้าที่เป็นผู้แนะนำการใช้งานครับ
          </p>
          <svg
            class="bg"
            xmlns="http://www.w3.org/2000/svg"
            width="603"
            height="197.833"
            viewBox="0 0 603 197.833"
          >
            <g
              id="Group_68"
              data-name="Group 68"
              transform="translate(-1128 -142)"
            >
              <rect
                id="Rectangle_8"
                data-name="Rectangle 8"
                width="603"
                height="169"
                rx="84.5"
                transform="translate(1128 142)"
                fill="#fff"
              />
              <path
                id="Path_63"
                data-name="Path 63"
                d="M1138.667,340s62.667,6.667,70.667-40"
                transform="translate(5 -9)"
                fill="none"
                stroke="#fff"
                stroke-linecap="round"
                stroke-width="17"
              />
            </g>
          </svg>
        </div>
      </div>
      <p class="btn-start">
        <span v-if="isLoading" class="active">INSERT USB TO START!</span>
        <router-link v-if="!isLoading" v-on:click="isInsert = true" to="/home" >LET'S START!</router-link><!--v-if="!isLoading" v-on:click="isInsert = true"-->
      </p>
    </div>
    <div class="hint active"> <!--v-if="isInsert"-->
      <div class="hint-ttl">
        <p class="icon op-btn">
          <svg
            class="off"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 36.572"
          >
            <g
              id="Group_103"
              data-name="Group 103"
              transform="translate(-1022 -151)"
            >
              <g id="light-bulb" transform="translate(1022 151)">
                <path
                  id="Path_64"
                  data-name="Path 64"
                  d="M16.57,27.5H7.428a1.072,1.072,0,0,1-1.048-.85c-.173-.819-.347-1.823-.515-2.795-.1-.581-.2-1.178-.305-1.729a12,12,0,1,1,12.879,0c-.1.551-.205,1.147-.305,1.728-.168.972-.341,1.976-.515,2.795a1.071,1.071,0,0,1-1.048.85Zm0,0"
                  transform="translate(0 0)"
                  fill="#bbfff1"
                />
                <path
                  id="Path_65"
                  data-name="Path 65"
                  d="M168,0V27.5h4.571a1.071,1.071,0,0,0,1.048-.85c.173-.819.347-1.823.514-2.795.1-.581.2-1.177.305-1.728A12,12,0,0,0,168,0Zm0,0"
                  transform="translate(-156)"
                  fill="#9fe8ff"
                />
                <path
                  id="Path_66"
                  data-name="Path 66"
                  d="M93.675,366.214a5.721,5.721,0,0,1-5.714-5.714v-4.429A1.071,1.071,0,0,1,89.032,355h9.289a1.071,1.071,0,0,1,1.071,1.071V360.5a5.722,5.722,0,0,1-5.717,5.714Zm0,0"
                  transform="translate(-81.678 -329.643)"
                  fill="#f5f0eb"
                />
                <path
                  id="Path_67"
                  data-name="Path 67"
                  d="M118.147,95.355a1.071,1.071,0,0,1-.835-1.742l2.813-3.5h-3.052a1.071,1.071,0,0,1-.84-1.737l3.934-4.968a1.071,1.071,0,1,1,1.68,1.331l-2.559,3.231h3.07a1.071,1.071,0,0,1,.836,1.742l-4.21,5.247A1.07,1.07,0,0,1,118.147,95.355Zm0,0"
                  transform="translate(-107.715 -77.07)"
                  fill="#6c9dff"
                />
                <path
                  id="Path_68"
                  data-name="Path 68"
                  d="M71.767,417.143H58.051a1.071,1.071,0,0,1,0-2.143H71.767a1.071,1.071,0,0,1,0,2.143Zm0,0"
                  transform="translate(-52.91 -385.357)"
                  fill="#ebe1dc"
                />
                <path
                  id="Path_69"
                  data-name="Path 69"
                  d="M71.767,357.143H58.051a1.071,1.071,0,1,1,0-2.143H71.767a1.071,1.071,0,1,1,0,2.143Zm0,0"
                  transform="translate(-52.91 -329.643)"
                  fill="#ebe1dc"
                />
                <path
                  id="Path_70"
                  data-name="Path 70"
                  d="M168,87.427l2.131-2.691a1.071,1.071,0,1,0-1.68-1.33l-.452.57Zm0,0"
                  transform="translate(-156 -77.07)"
                  fill="#6c9dff"
                />
                <path
                  id="Path_71"
                  data-name="Path 71"
                  d="M171.608,153.151a1.071,1.071,0,0,0-.966-.608H168v2.143h.409l-.409.51v3.424l3.479-4.335A1.071,1.071,0,0,0,171.608,153.151Zm0,0"
                  transform="translate(-156 -141.647)"
                  fill="#6c9dff"
                />
                <path
                  id="Path_72"
                  data-name="Path 72"
                  d="M172.643,355H168v11.214a5.722,5.722,0,0,0,5.714-5.714v-4.429A1.071,1.071,0,0,0,172.643,355Zm0,0"
                  transform="translate(-156 -329.643)"
                  fill="#ebe1dc"
                />
                <g
                  id="Group_11"
                  data-name="Group 11"
                  transform="translate(12 25.357)"
                >
                  <path
                    id="Path_73"
                    data-name="Path 73"
                    d="M174.857,355H168v2.143h6.857a1.071,1.071,0,1,0,0-2.143Zm0,0"
                    transform="translate(-168 -355)"
                    fill="#dcd2cd"
                  />
                  <path
                    id="Path_74"
                    data-name="Path 74"
                    d="M174.857,415H168v2.143h6.857a1.071,1.071,0,1,0,0-2.143Zm0,0"
                    transform="translate(-168 -410.714)"
                    fill="#dcd2cd"
                  />
                </g>
              </g>
            </g>
          </svg>
          <svg
            class="on"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 36.375 55.429"
          >
            <g id="light-bulb" transform="translate(0 0)">
              <path
                id="Path_64"
                data-name="Path 64"
                d="M25.115,41.68H11.258a1.624,1.624,0,0,1-1.589-1.288c-.263-1.241-.525-2.764-.78-4.236-.152-.881-.308-1.786-.463-2.621a18.191,18.191,0,1,1,19.519,0c-.155.834-.311,1.738-.463,2.619-.254,1.473-.517,3-.78,4.236a1.624,1.624,0,0,1-1.589,1.288Zm0,0"
                transform="translate(0 0)"
                fill="#ffd222"
              />
              <path
                id="Path_65"
                data-name="Path 65"
                d="M168,0V41.68h6.927a1.624,1.624,0,0,0,1.589-1.288c.263-1.241.526-2.763.78-4.236.152-.88.308-1.785.463-2.619A18.189,18.189,0,0,0,168,0Zm0,0"
                transform="translate(-149.813)"
                fill="#ecbd00"
              />
              <path
                id="Path_66"
                data-name="Path 66"
                d="M96.622,372a8.67,8.67,0,0,1-8.661-8.661v-6.712A1.624,1.624,0,0,1,89.585,355h14.078a1.624,1.624,0,0,1,1.624,1.624v6.712A8.673,8.673,0,0,1,96.622,372Zm0,0"
                transform="translate(-78.439 -316.568)"
                fill="#f5f0eb"
              />
              <path
                id="Path_67"
                data-name="Path 67"
                d="M119.253,101.727a1.624,1.624,0,0,1-1.265-2.64l4.263-5.312h-4.626a1.624,1.624,0,0,1-1.273-2.632l5.963-7.529a1.624,1.624,0,1,1,2.546,2.017l-3.878,4.9h4.653a1.624,1.624,0,0,1,1.267,2.64l-6.381,7.952A1.622,1.622,0,0,1,119.253,101.727Zm0,0"
                transform="translate(-103.443 -74.013)"
                fill="#fff16c"
              />
              <path
                id="Path_68"
                data-name="Path 68"
                d="M79.392,418.248H58.6a1.624,1.624,0,0,1,0-3.248H79.392a1.624,1.624,0,0,1,0,3.248Zm0,0"
                transform="translate(-50.812 -370.073)"
                fill="#ebe1dc"
              />
              <path
                id="Path_69"
                data-name="Path 69"
                d="M79.392,358.248H58.6a1.624,1.624,0,1,1,0-3.248H79.392a1.624,1.624,0,1,1,0,3.248Zm0,0"
                transform="translate(-50.812 -316.568)"
                fill="#ebe1dc"
              />
              <path
                id="Path_70"
                data-name="Path 70"
                d="M168,89.71l3.23-4.079a1.624,1.624,0,1,0-2.546-2.016l-.685.864Zm0,0"
                transform="translate(-149.813 -74.013)"
                fill="#f2de00"
              />
              <path
                id="Path_71"
                data-name="Path 71"
                d="M173.469,153.465a1.624,1.624,0,0,0-1.464-.921H168v3.248h.62l-.62.773v5.189l5.272-6.57A1.623,1.623,0,0,0,173.469,153.465Zm0,0"
                transform="translate(-149.812 -136.029)"
                fill="#f2de00"
              />
              <path
                id="Path_72"
                data-name="Path 72"
                d="M175.037,355H168v17a8.673,8.673,0,0,0,8.661-8.661v-6.712A1.624,1.624,0,0,0,175.037,355Zm0,0"
                transform="translate(-149.813 -316.568)"
                fill="#ebe1dc"
              />
              <g
                id="Group_11"
                data-name="Group 11"
                transform="translate(18.187 38.432)"
              >
                <path
                  id="Path_73"
                  data-name="Path 73"
                  d="M178.393,355H168v3.248h10.393a1.624,1.624,0,1,0,0-3.248Zm0,0"
                  transform="translate(-168 -355)"
                  fill="#dcd2cd"
                />
                <path
                  id="Path_74"
                  data-name="Path 74"
                  d="M178.393,415H168v3.248h10.393a1.624,1.624,0,1,0,0-3.248Zm0,0"
                  transform="translate(-168 -408.504)"
                  fill="#dcd2cd"
                />
              </g>
            </g>
          </svg>
        </p>
        <p class="ttl">เริ่มต้นการใช้งาน</p>
        <p class="btn-close op-btn">
          <svg
            id="cancel"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 46 46"
          >
            <circle
              id="Ellipse_6"
              data-name="Ellipse 6"
              cx="23"
              cy="23"
              r="23"
              transform="translate(0)"
              fill="#f15249"
            />
            <path
              id="Path_78"
              data-name="Path 78"
              d="M147.2,167.953l12.407,12.407a22.881,22.881,0,0,0,20.025-19.88L167.153,148Z"
              transform="translate(-133.85 -134.577)"
              fill="#ad0e0e"
            />
            <path
              id="Path_79"
              data-name="Path 79"
              d="M147.728,141.2a2.717,2.717,0,0,1,0,3.773L145.7,147a2.717,2.717,0,0,1-3.773,0l-15.962-15.962a2.716,2.716,0,0,1,0-3.773l2.1-2.1a2.717,2.717,0,0,1,3.773,0Z"
              transform="translate(-113.845 -113.118)"
              fill="#fff"
            />
            <path
              id="Path_80"
              data-name="Path 80"
              d="M221.877,216,216,221.877l8.489,8.416a2.716,2.716,0,0,0,3.773,0l2.1-2.1a2.716,2.716,0,0,0,0-3.773Z"
              transform="translate(-196.41 -196.41)"
              fill="#d6d6d6"
            />
            <path
              id="Path_81"
              data-name="Path 81"
              d="M141.924,125.962a2.716,2.716,0,0,1,3.773,0l2.1,2.1a2.716,2.716,0,0,1,0,3.773l-16.035,15.89a2.717,2.717,0,0,1-3.773,0l-2.032-2.032a2.716,2.716,0,0,1,0-3.773Z"
              transform="translate(-113.845 -113.845)"
              fill="#fff"
            />
          </svg>
        </p>
      </div>
      <div class="hint-txt">
        เริ่มต้นการใช้งานโดยนำ
        <span class="highlight">Thumb drive</span> มาเสียบเข้าที่ USB port
        จากนั้นกดปุ่ม
        <span class="img">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            width="164"
            height="51"
            viewBox="0 0 164 51"
          >
            <defs>
              <filter
                id="Rectangle_105"
                x="0"
                y="0"
                width="164"
                height="51"
                filterUnits="userSpaceOnUse"
              >
                <feOffset input="SourceAlpha" />
                <feGaussianBlur stdDeviation="3" result="blur" />
                <feFlood flood-opacity="0.161" />
                <feComposite operator="in" in2="blur" />
                <feComposite in="SourceGraphic" />
              </filter>
            </defs>
            <g
              id="Group_104"
              data-name="Group 104"
              transform="translate(-1788 -276)"
            >
              <g
                transform="matrix(1, 0, 0, 1, 1788, 276)"
                filter="url(#Rectangle_105)"
              >
                <rect
                  id="Rectangle_105-2"
                  data-name="Rectangle 105"
                  width="146"
                  height="33"
                  rx="16.5"
                  transform="translate(9 9)"
                  fill="#fff"
                />
              </g>
              <text
                id="LET_S_START_"
                data-name="LET’S START!"
                transform="translate(1870 306)"
                fill="#333"
                font-size="14"
                font-family="ArialRoundedMTBold, Arial Rounded MT"
              >
                <tspan x="-47.701" y="0">LET’S START!</tspan>
              </text>
            </g>
          </svg>
        </span>
      </div>
      <div class="hint-img">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 149.328 107.756">
          <g id="usb_1_" data-name="usb (1)" transform="translate(0 -71.269)">
            <path
              id="Path_194"
              data-name="Path 194"
              d="M143.474,71.907l-92.288,53.56v23.624L93.3,173.4l92.287-53.56V96.22Z"
              transform="translate(-36.257 -0.452)"
              fill="#3e3d43"
            />
            <g
              id="Group_98"
              data-name="Group 98"
              transform="translate(17.94 95.582)"
            >
              <path
                id="Path_195"
                data-name="Path 195"
                d="M61.511,291.072v-16.4l35.854,20.7v16.4Z"
                transform="translate(-61.511 -239.661)"
                fill="#2e2e30"
              />
              <path
                id="Path_196"
                data-name="Path 196"
                d="M195.171,208.191l92.288-53.56v23.625l-92.288,53.56Z"
                transform="translate(-156.188 -154.631)"
                fill="#2e2e30"
              />
            </g>
            <path
              id="Path_197"
              data-name="Path 197"
              d="M216.624,238.184l79.774-46.3v9.156l-79.774,46.3Z"
              transform="translate(-153.444 -85.438)"
              fill="#1d1d1f"
            />
            <path
              id="Path_198"
              data-name="Path 198"
              d="M50.784,124.829l92.288-53.56,42.111,24.313L92.9,149.142Z"
              transform="translate(-35.973 0)"
              fill="#57565c"
            />
            <g
              id="Group_99"
              data-name="Group 99"
              transform="translate(48.086 92.239)"
            >
              <path
                id="Path_199"
                data-name="Path 199"
                d="M226.132,144.567a12.857,12.857,0,0,0-11.666,0c-2.581,1.5-3.074,3.75-1.489,5.543l-13.12,7.624H181.326a3.678,3.678,0,0,0-1.806.434l-4.9,2.846-2.057-1.187-7.691,4.47,7.742,4.469,7.691-4.47-2.057-1.187L182.4,160.7h12.358l-20.284,11.788-3.993-2.306L166.4,179.1l15.391-2.391L178.1,174.58l30.184-17.541.039,6.81-8.309,4.829a10.056,10.056,0,0,0-6.9.83c-2.5,1.454-2.489,3.811.029,5.265a10.017,10.017,0,0,0,9.09,0c1.861-1.081,2.328-2.662,1.41-4l9.055-5.262a1.273,1.273,0,0,0,.744-1.048l-.06-10.386,3.221-1.872a13,13,0,0,0,9.564-.881c3.21-1.866,3.193-4.891-.038-6.757"
                transform="translate(-164.874 -143.167)"
                fill="#3e3d43"
              />
            </g>
            <path
              id="Path_200"
              data-name="Path 200"
              d="M26.573,291.767,0,307.21v12.4l27.017,15.6,26.777-15.561v-12.17Zm-.492,41.855.029-.017v.017Z"
              transform="translate(0 -156.189)"
              fill="#898890"
            />
            <g
              id="Group_100"
              data-name="Group 100"
              transform="translate(0 135.578)"
            >
              <path
                id="Path_201"
                data-name="Path 201"
                d="M3.087,312.378l26.777-15.561-.029,10.266L3.087,322.644Z"
                transform="translate(-2.187 -295.344)"
                fill="#77767e"
              />
              <path
                id="Path_202"
                data-name="Path 202"
                d="M85.494,376.557,112.271,361l-.011,3.871L85.494,380.428Z"
                transform="translate(-60.559 -340.805)"
                fill="#2e2e30"
              />
              <path
                id="Path_203"
                data-name="Path 203"
                d="M7.1,331.294l26.777-15.561,22.865,13.2L29.962,344.5Z"
                transform="translate(-5.027 -308.743)"
                fill="#57565c"
              />
              <path
                id="Path_204"
                data-name="Path 204"
                d="M0,344.717l27.017,15.6v12.4L0,357.122Zm26.111,26.412V360.863L.9,346.308v10.266l25.182,14.555"
                transform="translate(0 -329.274)"
                fill="#acabb1"
              />
              <path
                id="Path_205"
                data-name="Path 205"
                d="M29.962,382.289v3.871L7.1,372.959v-3.871Z"
                transform="translate(-5.027 -346.537)"
                fill="#3e3d43"
              />
              <path
                id="Path_206"
                data-name="Path 206"
                d="M92.632,360.974l26.777-15.326-.035,12.17L92.632,373.38Z"
                transform="translate(-65.615 -329.933)"
                fill="#898890"
              />
              <path
                id="Path_207"
                data-name="Path 207"
                d="M0,307.21l26.573-15.443,27.221,15.715L27.017,322.808Z"
                transform="translate(0 -291.767)"
                fill="#c6c5cb"
              />
            </g>
            <path
              id="Path_208"
              data-name="Path 208"
              d="M50.093,331.024a.158.158,0,0,1,0,.3l-4.562,2.651a.568.568,0,0,1-.516,0l-6-3.466a.158.158,0,0,1,0-.3l4.562-2.651a.569.569,0,0,1,.516,0l6,3.466m12.171,7.027-6-3.466a.568.568,0,0,0-.516,0l-4.562,2.651a.158.158,0,0,0,0,.3l6,3.466a.568.568,0,0,0,.516,0l4.562-2.651a.158.158,0,0,0,0-.3"
              transform="translate(-27.559 -181.497)"
              fill="#77767e"
            />
            <g
              id="Group_101"
              data-name="Group 101"
              transform="translate(14.618 147.887)"
            >
              <path
                id="Path_209"
                data-name="Path 209"
                d="M52.96,338.559a.568.568,0,0,0,.516,0l4.562-2.651a.158.158,0,0,0,0-.3l-2.84-1.64-5.076,2.95Z"
                transform="translate(-50.12 -333.969)"
                fill="#57565c"
              />
              <path
                id="Path_210"
                data-name="Path 210"
                d="M87.263,358.067l4.562-2.651a.158.158,0,0,0,0-.3l-6-3.466a.568.568,0,0,0-.516,0L80.742,354.3a.158.158,0,0,0,0,.3l6,3.466A.568.568,0,0,0,87.263,358.067Z"
                transform="translate(-71.736 -346.45)"
                fill="#57565c"
              />
            </g>
            <path
              id="Path_211"
              data-name="Path 211"
              d="M235.9,327.65c.006,2.016.717,3.435,1.865,4.1L242.5,334.5l-.013-.008c1.164.684,2.779.592,4.563-.437a14.046,14.046,0,0,0,6.374-11.04c-.006-2.022-.722-3.443-1.876-4.108l.011.006-4.737-2.753c-1.163-.676-2.773-.581-4.55.446A14.046,14.046,0,0,0,235.9,327.65Z"
              transform="translate(-167.098 -173.165)"
              fill="#898890"
            />
            <path
              id="Path_212"
              data-name="Path 212"
              d="M267.042,318.918l-4.737-2.753c-1.163-.676-2.773-.581-4.55.446l4.737,2.753C264.269,318.337,265.879,318.242,267.042,318.918Z"
              transform="translate(-182.579 -173.165)"
              fill="#c6c5cb"
            />
            <path
              id="Path_213"
              data-name="Path 213"
              d="M237.765,333.882l4.737,2.753c-1.148-.667-1.86-2.085-1.865-4.1a14.047,14.047,0,0,1,6.374-11.04l-4.737-2.753a14.048,14.048,0,0,0-6.374,11.04C235.906,331.8,236.617,333.215,237.765,333.882Z"
              transform="translate(-167.098 -175.296)"
              fill="#acabb1"
            />
            <path
              id="Path_214"
              data-name="Path 214"
              d="M258.516,326.048a14.047,14.047,0,0,0-6.374,11.04c.012,4.059,2.884,5.695,6.416,3.656a14.046,14.046,0,0,0,6.374-11.04C264.92,325.646,262.047,324.009,258.516,326.048Z"
              transform="translate(-178.603 -179.85)"
              fill="#898890"
            />
            <path
              id="Path_215"
              data-name="Path 215"
              d="M264.6,336.743a8.549,8.549,0,0,0-3.879,6.719c.007,2.47,1.755,3.466,3.9,2.225a8.549,8.549,0,0,0,3.879-6.719C268.5,336.5,266.751,335.5,264.6,336.743Z"
              transform="translate(-184.682 -187.669)"
              fill="#77767e"
            />
          </g>
        </svg>
      </div>
    </div>
    <svg
      class="bg-shadow"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 1807.987 884.553"
    >
      <path
        id="Subtraction_4"
        data-name="Subtraction 4"
        d="M119-3761.947h0v-884.21l.393-.168.406-.174H1926.987l-.092.343c-3.666,13.609-7.726,27.266-12.068,40.588-4.3,13.182-8.992,26.413-13.956,39.326a805.2,805.2,0,0,1-33.309,74.948c-12.066,23.793-25.546,47.392-40.064,70.142-14.189,22.233-29.761,44.269-46.285,65.494-16.136,20.728-33.623,41.253-51.975,61.006-17.9,19.27-37.125,38.339-57.133,56.677-19.5,17.872-40.277,35.537-61.758,52.507-20.917,16.524-43.073,32.841-65.853,48.5-22.161,15.231-45.516,30.252-69.414,44.646-23.222,13.986-47.6,27.766-72.444,40.955-24.111,12.8-49.325,25.388-74.942,37.422-24.819,11.659-50.694,23.115-76.908,34.049-25.357,10.577-51.715,20.951-78.342,30.835-25.714,9.545-52.375,18.892-79.245,27.781-25.9,8.567-52.682,16.94-79.614,24.885-25.894,7.64-52.626,15.092-79.452,22.149-50.361,13.249-102.945,25.607-156.291,36.729-48.5,10.112-98.72,19.43-149.26,27.7-85.127,13.923-172.74,25.159-260.4,33.4-34.445,3.236-68.975,6.011-102.632,8.247-26.919,1.789-53.356,3.24-78.577,4.313C144.529-3762.063,120.023-3761.951,119-3761.947Z"
        transform="translate(-119 4646.5)"
        fill="#333"
        opacity="0.12"
      />
    </svg>
  </div>
</template>

<script>
import $ from "jquery";
import axios from 'axios'
var axiosInstance = axios.create({
    baseURL: `${location.protocol}//${location.hostname}:3000`,
})
export default {
  name: "HelloWorld",
  data() {
    return {
      name: "LoadingScreen",
      isInsert: false,
      //props: ["isLoading"]
      isLoading: true
    };
  },
  mounted() {
        /*setTimeout(() => {
            this.isLoading = false;
        }, 3000);*/
        const intervalObj = setInterval(() => {
            axiosInstance.get('getDrive').then((response) => {
              console.log(response.data.drives)
              if(response.data.drives === 'OK'){
                this.isLoading = false;
                console.log(response.data.mountPoints.path)
                this.$store.commit('setUsbPath', response.data.mountPoints.path)
                clearInterval(intervalObj);
              }
            })
        }, 1500);
    }



};

$(document).ready(function() {
  $(".hint .btn-close, .hint .icon svg").click(function() {
    $(".hint").toggleClass("active");
  });
});


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
.op-btn {
  transition: opacity 0.3s ease-in;
  cursor: pointer;
  &:hover {
    opacity: 0.7;
  }
}
.hello {
  position: relative;
  height: 100vh;
  background-color: $primary-color;
}
.panel {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  height: 100%;
  .mascot {
    position: relative;
    img {
      width: 500px;
    }
    .balloon {
      position: absolute;
      top: -32px;
      right: -274px;
      z-index: 1;
      .txt {
        position: absolute;
        top: 60px;
        left: 40px;
        height: 100%;
        width: 100%;
        font-size: 1.2rem;
        text-align: left;
        span {
          &.highlight {
            color: $primary-color;
            font-weight: 600;
          }
          &.name {
            color: #f15249;
            font-weight: 600;
          }
        }
      }
      svg {
        width: 460px;
      }
    }
  }
  .btn-start {
    margin-top: 30px;
    a {
      color: unset;
      text-decoration: none;
    }
    a,span {
      cursor: pointer;
      display: block;
      border-radius: 46px;
      background: #fff;
      padding: 10px 40px;
      box-shadow: 0px 0px 6px #00000029;
      font-weight: 800;
      font-size: 1.4rem;
      transition: opacity 0.3s ease-in;
      text-align: center;
      &:hover {
        opacity: 0.7;
      }
    }
  }
}
.hint {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 400px;
  background: #444444;
  border-radius: 38px;
  padding: 20px;
  overflow: hidden;
  clip-path: circle(29px at 32px 39px);
  z-index: 1;
  transition: clip-path 0.3s ease-in;

  .hint-ttl {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    .icon {
      margin-right: 10px;
      svg {
        width: 25px;
        &.on {
          display: none;
        }
        &.off {
          display: block;
        }
      }
    }
    .ttl {
      font-weight: 800;
      font-size: 1.4rem;
      opacity: 0;
      transition: opacity 0.3s ease-in;
    }
    .btn-close {
      position: absolute;
      top: 20px;
      right: 20px;
      opacity: 0;
      transition: opacity 0.3s ease-in;
      svg {
        width: 30px;
      }
    }
  }
  .hint-txt {
    line-height: 1;
    opacity: 0;
    transition: opacity 0.3s ease-in;
    text-align: left;
    .highlight {
      color: $primary-color;
      font-weight: 600;
    }
    .img {
      svg {
        width: 120px;
      }
    }
  }
  .hint-img {
    text-align: center;
    margin: 20px 0;
    opacity: 0;
    transition: opacity 0.3s ease-in;
    svg {
      width: 120px;
    }
  }

  &.active {
    background: #fff7d6 0% 0% no-repeat padding-box;
    clip-path: circle(1000px at 32px 39px);
    .hint-ttl {
      .icon {
        svg {
          &.on {
            display: block;
          }
          &.off {
            display: none;
          }
        }
      }
      .ttl {
        opacity: 1;
      }
      .btn-close {
        opacity: 1;
      }
    }
    .hint-txt {
      opacity: 1;
    }
    .hint-img {
      opacity: 1;
    }
  }
}
.bg-shadow {
  position: absolute;
  top: 0;
  left: 0;
  width: 80%;
  pointer-events: none;
}
</style>
