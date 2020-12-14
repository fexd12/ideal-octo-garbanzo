<template>
  <div className="container">
    <div class="row justify-content-center py-5">
      <b-form-group label-cols-sm="2" label-size="sm">
        <b-img style="padding-bottom: 50px" id="preview" :src="imagem" alt="" />

        <span v-if="!imagem" class="placeholder"> Choose an Image </span>

        <b-form-file
          type="file"
          accept="image/*"
          id="file-input"
          size="sm"
          @change="upload_picture($event)"
        />
        <div class="botao">
          <b-button size="sm" @click="uploadImage()"> Enviar </b-button>
        </div>
      </b-form-group>
    </div>

		<div class="botao" v-if="response">
			<span>Texto enviado</span>
		</div>
  </div>
</template>

<script>
export default {
  name: "Blank",
  data: () => {
    return {
			imagem: null,
			response:null
    };
  },
  methods: {
    uploadImage() {
      // const URL = "http://localhost:3002/upload/";
      // let config = {
      //   header: {
      //     "Content-Type": "application/json",
      //   },
			// };
			
			// let data = {
			// 	imagem : this.imagem
			// };

			this.response = true
			console.log(this.response)
      // this.$http.post(URL, data, config).then((response) => {
      //   console.log("image upload response > ", response);
      // });
    },
    upload_picture(event) {

			let reader = new FileReader();

			reader.addEventListener("load",()=>{
				this.imagem = reader.result;
			},false);

			reader.readAsDataURL(event.target.files[0]);			
    },
  },
};
</script>

<style >
#preview {
  max-width: 100%;
  max-height: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.botao {
  border-radius: 6px solid #eee;
  padding-top: 5px;
  text-align: center;
}
</style>
