<template>
  <div class="signup-container">
    <div class="signup-form">
      <h2>Sign Up</h2>
      <form @submit.prevent="handleSignup">
        <div class="form-group">
          <label for="username">Username</label>
          <input 
            type="text" 
            id="username" 
            v-model="username" 
            required
            placeholder="Choose a username"
          >
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input 
            type="email" 
            id="email" 
            v-model="email" 
            required
            placeholder="Enter your email"
          >
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input 
            type="password" 
            id="password" 
            v-model="password" 
            required
            placeholder="Choose a password"
          >
        </div>

        <div v-if="error" class="error-message">
          {{ error }}
        </div>

        <button type="submit" class="submit-btn" :disabled="loading">
          {{ loading ? 'Creating account...' : 'Sign Up' }}
        </button>
      </form>
      <p class="login-link">
        Already have an account? 
        <router-link to="/login">Login here</router-link>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { authApi } from '../services/api'

const router = useRouter()
const username = ref('')
const email = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

const handleSignup = async () => {
  try {
    loading.value = true
    error.value = ''
    
    await authApi.signup(username.value, email.value, password.value)
    
    // Redirect to login page after successful signup
    router.push('/login')
  } catch (err: any) {
    error.value = err.response?.data?.detail || 'An error occurred during signup'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.signup-container {
  width: 100%;
  min-height: calc(100vh - 80px);
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f5f5f5;
  padding: 2rem 0;
}

.signup-form {
  background-color: white;
  padding: 3rem 4rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}

h2 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 3rem;
  font-size: 2.5rem;
}

.form-group {
  margin-bottom: 2rem;
}

label {
  display: block;
  margin-bottom: 0.8rem;
  color: #2c3e50;
  font-weight: 500;
  font-size: 1.2rem;
}

input {
  width: 100%;
  padding: 1rem;
  border: 2px solid #ddd;
  border-radius: 6px;
  font-size: 1.1rem;
  transition: border-color 0.3s;
}

input:focus {
  outline: none;
  border-color: #2c3e50;
}

.submit-btn {
  width: 100%;
  padding: 1rem;
  background-color: #2c3e50;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 2rem;
}

.submit-btn:hover {
  background-color: #34495e;
}

.submit-btn:disabled {
  background-color: #95a5a6;
  cursor: not-allowed;
}

.error-message {
  color: #e74c3c;
  text-align: center;
  margin-bottom: 1rem;
  padding: 1rem;
  border-radius: 6px;
  background-color: #fde8e8;
  font-size: 1.1rem;
}

.login-link {
  text-align: center;
  margin-top: 2rem;
  color: #666;
  font-size: 1.1rem;
}

.login-link a {
  color: #2c3e50;
  text-decoration: none;
  font-weight: 500;
}

.login-link a:hover {
  text-decoration: underline;
}
</style>