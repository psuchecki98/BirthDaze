import React, { useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import 'tailwindcss/tailwind.css';

import NavBar from './Navbar';
import UserContext from '../Context/UserContext';

function SignIn() {

    const navigate = useNavigate();
    const { setUser } = useContext(UserContext);

    const [formData, setFormData] = useState({
        email: '',
        password_hash: ''
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const response = await fetch('http://127.0.0.1:5555/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();

        if (data.success) {
            setUser(formData.email);
            navigate('/user');
        }
        else {
            alert('Invalid credentials');
        }
    };

    return (
        <div className="flex flex-col justify-center h-screen bg-white">
            <div className='border-y-2'>
                <NavBar />
            </div>
            <div className="m-auto w-1/3 text-white flex flex-wrap justify-center shadow-lg rounded-lg bg-gray-800 bg-opacity-2">
                <form className="m-5 w-10/12" onSubmit={handleSubmit}>
                    <h1 className="w-full text-5xl font-bold text-center border-y-2 my-6">
                        Welcome back !
                    </h1>
                    <h2 className="w-full text-sm italic text-left">
                        Please enter your login information:
                    </h2>
                    <div className="w-full my-6">
                        <input
                            type="email"
                            className="p-2 rounded shadow w-full text-black"
                            placeholder="Enter Email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="w-full my-6">
                        <input
                            type="password"
                            className="p-2 rounded shadow w-full text-black"
                            placeholder="Enter Password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                        />
                    </div>
                    <div className="w-full my-10">
                        <button type="submit" className="p-2 rounded shadow w-full bg-blue-500 hover:bg-blue-600 text-black">
                            Sign In
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default SignIn;
