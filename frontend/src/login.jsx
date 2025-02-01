import React, { useState } from "react";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!email || !password) {
      setError("Please fill in all fields");
      return;
    }
    console.log("Logging in with", email, password);
    setError(null);
  };

  return (
    <div className="login-container d-flex justify-content-center align-items-center vh-100" style={{ backgroundColor: "#f0f0f0" }}>
      <form className="login-form bg-white p-4 rounded shadow-sm" style={{ width: "300px", maxWidth: "80%" }} onSubmit={handleSubmit}>
        <div className="form-header text-center mb-3">
          <h2>Login to Your Gmail Account</h2>
        </div>

        {error && <p className="text-danger text-center">{error}</p>}

        <div className="mb-3">
          <label htmlFor="email" className="form-label fw-bold">Email:</label>
          <input
            type="text"
            id="email"
            className="form-control"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>

        <div className="mb-3">
          <label htmlFor="password" className="form-label fw-bold">Password:</label>
          <input
            type="password"
            id="password"
            className="form-control"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        <div className="mb-3">
          <button type="submit" className="btn btn-primary w-100">Login</button>
        </div>
      </form>
    </div>
  );
};

export default Login;
