<template>
  <div className="container">
    <div class="row justify-content-center py-5">
			<b-form-group label-cols-sm="2" label-size="sm">
				<b-img id="preview" :src="url" alt="" />

				<span
					v-if="!url"
					class="placeholder"
				>
					Choose an Image
				</span>

				<b-form-file
					type="file"
					accept="image/*"
					id="file-input"
					size="sm"
					@change="upload_picture($event)"
				/>

			</b-form-group>

			<b-form-group label-cols-sm="2" label-size="sm">
				<b-button size="sm" @click="uploadImage()"> Enviar </b-button>
			</b-form-group>
      
    </div>
  </div>
</template>

<script>
export default {
  name: "Blank",
  data:() => {
    return {
			imagem: [],
			url:''
    };
  },
  methods: {
    uploadImage() {
      const URL = "http://foobar.com/upload";

      let config = {
        header: {
          "Content-Type": "image/png",
        },
      };

      this.$http.put(URL,this.imagem, config).then((response) => {
        console.log("image upload response > ", response);
      });
    },
    upload_picture(event) {
			let data = {
				name: event.target.files[0].name,
				file : event.target.files[0]
			}
			this.imagem.push(data);
			this.url = URL.createObjectURL(data.file)
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
</style>
