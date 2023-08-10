import React, { useState } from 'react';
import 'tailwindcss/tailwind.css';

import NavBar from './Navbar';

function SignUp() {

    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: ''
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
    };

    return (
        <div className="flex flex-col justify-center h-screen bg-white">
            <div className='border-y-2'>
                <NavBar />
            </div>
            <div className="m-auto w-1/3 text-white flex flex-wrap justify-center shadow-lg rounded-lg bg-gray-800 bg-opacity-2">
                <form className="m-5 w-10/12" onSubmit={handleSubmit}>
                    <h1 className="w-full text-4xl text-center font-bold border-y-2 my-6">
                        SIGN UP
                    </h1>
                    <h2 className='w-full text-sm text-left italic'>
                        Enter the following to create an account:
                    </h2>
                    <div className="w-full my-6">
                        <input 
                            type="text"
                            className="p-2 rounded shadow w-full text-black"
                            placeholder="Username"
                            name="username"
                            value={formData.username}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="w-full my-6">
                        <input 
                            type="email"
                            className="p-2 rounded shadow w-full text-black"
                            placeholder="Email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="w-full my-6">
                        <input 
                            type="password"
                            className="p-2 rounded shadow w-full text-black"
                            placeholder="Password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                        />
                    </div>
                    <h2 class="mb-2 text-lg font-semibold text-gray-900 dark:text-white">Account requirements:</h2>
                    <ul class="max-w-md space-y-1 text-gray-500 list-inside dark:text-gray-400">
                        <li class="flex items-center">
                            <svg class="w-3.5 h-3.5 mr-2 text-green-500 dark:text-green-400 flex-shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z"/>
                            </svg>
                             Username between 5-16 characters
                        </li>
                        <li class="flex items-center">
                            <svg class="w-3.5 h-3.5 mr-2 text-green-500 dark:text-green-400 flex-shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z"/>
                            </svg>
                            Email must end in .com, .org, or .net
                        </li>
                        <li class="flex items-center">
                            <svg class="w-3.5 h-3.5 mr-2 text-gray-500 dark:text-gray-400 flex-shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z"/>
                            </svg>
                            Password between 5-16 characters
                        </li>
                    </ul>
                    <div className="w-full my-10">
                        <button type="submit" className="p-2 rounded shadow w-full bg-blue-500 hover:bg-blue-600 text-black">
                            Create Account
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default SignUp;