'use client';

import { useState } from "react";
import { Lock, Mail } from "lucide-react";

export default function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();
    console.log("Email:", email, "Password:", password);
  };

  return (
    <div className="w-full max-w-md bg-white shadow-lg rounded-2xl p-8 text-center">
      {/* Logo */}
      <div className="mb-6">
        <img src="/images/logo.png" alt="proDP Logo" className="h-12 mx-auto" />
      </div>

      <h2 className="text-2xl font-semibold text-gray-800">Connexion</h2>
      <p className="text-gray-500 mb-6">Accédez à votre compte</p>

      <form onSubmit={handleLogin} className="space-y-4">
        {/* Email Input */}
        <div className="relative">
          <Mail className="absolute left-3 top-3 text-gray-400 w-5 h-5" />
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full pl-10 pr-4 py-3 rounded-lg bg-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        {/* Password Input */}
        <div className="relative">
          <Lock className="absolute left-3 top-3 text-gray-400 w-5 h-5" />
          <input
            type="password"
            placeholder="Mot de passe"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full pl-10 pr-4 py-3 rounded-lg bg-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        {/* Login Button */}
        <button
          type="submit"
          className="w-full bg-blue-600 text-white font-semibold py-3 rounded-lg hover:bg-blue-700 transition"
        >
          Se connecter
        </button>
      </form>

      {/* Footer Links */}
      <div className="mt-4 text-sm">
        <a href="#" className="text-blue-600 hover:underline">
          Mot de passe oublié ?
        </a>
      </div>
    </div>
  );
}
