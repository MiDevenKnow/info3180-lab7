<template>
<div class="container">
    <h1>Upload Form</h1>
    <form id="uploadForm" @submit.prevent="uploadPhoto">
        <div id = "message">
            <p class="alert alert-success" v-if="message === 'success'" >{{success}}</p>
            <ul class="alert alert-danger" v-if="message === 'error'" >
                <li v-for="error in errors" :key="error"> {{error}}</li>
            </ul> 
        </div>
        <div class="mb-3">
            <label for="exampleFormControlTextarea1" class="form-label">Description</label>
            <textarea name="description" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
        </div>
        <div class="mb-3">
            <label for="formFile" class="form-label">Photo Upload</label>
            <input name="photo" class="form-control" type="file" id="formFile">
        </div>
        <div>
            <button type="submit" class="btn btn-primary mb-3">Submit</button>
        </div>
    </form>
</div>
</template>

<script>
export default {
    data() {
        return {
            csrf_token: '',
            message: '',
            errors: [],
            success:[]
        }
    },
    methods: {
        uploadPhoto(){
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
            let self = this;
            fetch("/api/upload", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                if ('success' in data ){
                    self.success = data.success.message;
                    self.message = 'success';
                    console.log("success")
                    console.log(self.success)
                } else if ('error' in data ){
                    self.errors = data.error.errors;
                    self.message = 'error';
                    console.log("error")
                    console.log(self.errors)
                }
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')

            .then((response) => response.json())

            .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        }
    },
    created() {
        this.getCsrfToken();
    },
}
</script>