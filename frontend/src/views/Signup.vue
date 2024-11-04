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
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  padding: 1.5rem;
}

.signup-form {
  background-color: white;
  padding: 2.5rem 2rem;
  border-radius: 16px;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05),
              0 8px 10px -6px rgba(0, 0, 0, 0.03);
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  position: relative;
  overflow: hidden;
}

.signup-form::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, #3b82f6, #2563eb);
}

h2 {
  text-align: center;
  color: #1e293b;
  margin-bottom: 2rem;
  font-size: 1.75rem;
  font-weight: 600;
  letter-spacing: -0.025em;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #475569;
  font-weight: 500;
  font-size: 0.875rem;
  letter-spacing: 0.025em;
}

input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 0.95rem;
  transition: all 0.2s ease;
  background-color: #f8fafc;
}

input:hover {
  border-color: #cbd5e1;
}

input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
  background-color: white;
}

input::placeholder {
  color: #94a3b8;
}

.submit-btn {
  width: 100%;
  padding: 0.875rem;
  background: linear-gradient(90deg, #3b82f6, #2563eb);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-top: 1.5rem;
  position: relative;
  overflow: hidden;
}

.submit-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
}

.submit-btn:active {
  transform: translateY(0);
}

.submit-btn:disabled {
  background: #94a3b8;
  transform: none;
  box-shadow: none;
}

.error-message {
  color: #ef4444;
  text-align: center;
  margin: 1rem 0;
  padding: 0.75rem;
  border-radius: 8px;
  background-color: #fef2f2;
  font-size: 0.875rem;
  border: 1px solid #fee2e2;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.login-link {
  text-align: center;
  margin-top: 1.5rem;
  color: #64748b;
  font-size: 0.875rem;
  padding-top: 1rem;
  border-top: 1px solid #e2e8f0;
}

.login-link a {
  color: #3b82f6;
  text-decoration: none;
  font-weight: 500;
  margin-left: 0.25rem;
  transition: color 0.2s ease;
}

.login-link a:hover {
  color: #2563eb;
}

/* Optional: Add animation for form appearance */
@keyframes formAppear {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.signup-form {
  animation: formAppear 0.3s ease-out;
}
</style>