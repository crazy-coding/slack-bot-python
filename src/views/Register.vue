<template>
  <div>
    <b-row>
      <b-col
        lg="4" 
        offset-lg="4"
      >
        <h3> Create an Account:</h3>
      </b-col>
    </b-row>
    <b-row>
      <b-col 
        lg="4" 
        offset-lg="4"
      >
        <b-form 
          v-if="show"
          @submit="onSubmit"
        >
          <b-form-group
            id="input-group-email"
            label="Email address:"
            label-for="input-email"
            description="Please enter your email address."
          >
            <b-form-input
              id="input-email"
              v-model="form.email"
              type="email"
              required
              placeholder="Email address"
            />
          </b-form-group>

          <b-form-group 
            id="input-group-name" 
            label="Your Name:"
            label-for="input-name"
          >
            <b-row>
              <b-col md="6">
                <b-form-input
                  id="input-first-name"
                  v-model="form.lastName"
                  required
                  placeholder="First name"
                />
              </b-col>
              <b-col md="6">
                <b-form-input
                  id="input-last-name"
                  v-model="form.firstName"
                  required
                  placeholder="Last name"
                />
              </b-col>
            </b-row>
          </b-form-group>

          <b-form-group 
            id="input-group-password" 
            label="Please enter a password:"
            label-for="input-password"
            required
            placeholder="Password"
            description="Use a strong unique password, preferably created by a password manager."
          >
            <b-form-input
              id="input-password"
              type="password"
              v-model="form.password"
              required
            />
          </b-form-group>

          <b-form-group id="input-group-checkboxes">
            <b-form-checkbox-group
              id="checked-tos"
              v-model="form.checkedTOS"
              required
            >
              <b-form-checkbox 
                name="terms-of-service"
                value="terms-of-service"
              >
                I agree to the terms of service
              </b-form-checkbox>
              <b-form-invalid-feedback>Please select review and agree to the terms of service.</b-form-invalid-feedback>
            </b-form-checkbox-group>
            <b-form-checkbox-group
              id="checked-newsletter"
              v-model="form.checkedNewsletter"
            >
              <b-form-checkbox 
                value="newsletter"
              >
                Sign me up for your newsletter (optional)
              </b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
          <b-button 
            type="submit" 
            variant="primary"
          >
            Submit
          </b-button>
        </b-form>
        <b-card
          class="mt-3"
          header="Form Data Result"
        >
          <pre class="m-0">{{ form }}</pre>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        form: {
          email: '',
          firstName: '',
          lastName: '',
          password: null,
          checkedTOS: [],
          checkedNewsletter: []
        },
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
      }
    }
  }
</script>