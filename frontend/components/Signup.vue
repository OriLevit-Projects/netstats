<template>
  <div class="signup-container">
    <div class="signup-form">
      <h2>Create Account</h2>
      <!-- ... rest of the template remains the same ... -->
    </div>
  </div>
</template>

<style scoped>
.signup-container {
  min-height: calc(100vh - 80px);
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f8fafc;
  padding: 1.5rem;
}

.signup-form {
  background-color: white;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
              0 2px 4px -1px rgba(0, 0, 0, 0.06);
  width: 100%;
  max-width: 400px;
}

h2 {
  text-align: center;
  color: #1e293b;
  margin-bottom: 2rem;
  font-size: 1.875rem;
  font-weight: 600;
}

.form-group {
  margin-bottom: 1.5rem;
  position: relative;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #475569;
  font-weight: 500;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.025em;
}

input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.2s;
  background-color: #f8fafc;
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
  padding: 0.75rem;
  background-color: #3b82f6;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  margin-top: 1.5rem;
}

.submit-btn:hover {
  background-color: #2563eb;
  transform: translateY(-1px);
}

.submit-btn:disabled {
  background-color: #94a3b8;
  cursor: not-allowed;
  transform: none;
}

.error-message {
  color: #ef4444;
  text-align: center;
  margin-bottom: 1rem;
  padding: 0.75rem;
  border-radius: 8px;
  background-color: #fef2f2;
  font-size: 0.875rem;
  border: 1px solid #fee2e2;
}

.login-link {
  text-align: center;
  margin-top: 1.5rem;
  color: #64748b;
  font-size: 0.875rem;
}

.login-link a {
  color: #3b82f6;
  text-decoration: none;
  font-weight: 500;
  margin-left: 0.25rem;
}

.login-link a:hover {
  color: #2563eb;
  text-decoration: underline;
}

/* Optional: Add password strength indicator */
.password-strength {
  height: 4px;
  width: 100%;
  background: #e2e8f0;
  margin-top: 0.5rem;
  border-radius: 2px;
  overflow: hidden;
}

.password-strength-bar {
  height: 100%;
  width: 0;
  transition: width 0.3s, background-color 0.3s;
}

.strength-weak { background-color: #ef4444; width: 33%; }
.strength-medium { background-color: #f59e0b; width: 66%; }
.strength-strong { background-color: #10b981; width: 100%; }
</style> 