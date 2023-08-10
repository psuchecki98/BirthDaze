import React from 'react'
import { NavLink } from 'react-router-dom';
import 'tailwindcss/tailwind.css';


function HomePage() {

    return (
        <nav>
            <div className="flex h-screen bg-white">
                {/* Left side */}
                <div className="flex items-center justify-center w-1/2 bg-white">
                    <img src="https://ali-practice-aws-bucket.s3.amazonaws.com/Birthdaze_logo-removebg-preview.png" alt="Logo" className="w-[65%]" />
                </div>
        
                {/* Right side */}
                <div className="flex flex-col justify-center w-1/2 border-l-2 bg-white">
                    <h1 className="mb-4 text-5xl ml-4 font-bold text-gray-700">
                        Never forget a birthday again
                    </h1>
                    <h2 className='mb-20 text-2xl ml-4 border-b-2 font-bold text-blue-500 text-left'>
                        Join Today.
                    </h2>
                    <div className='ml-[20%]'>
                        <NavLink key={"SignIn"} name={"SignIn"} to={"/signin"}>
                            <button className="px-4 py-2 mb-2 w-3/4 self-center text-white bg-blue-500 rounded hover:bg-blue-600">
                                Sign in
                            </button>
                        </NavLink>
                    </div>
                    <div className="mb-4 text-2l font-bold text-center text-gray-700">
                        OR
                    </div>
                    <div className='ml-[20%]'>
                        <NavLink key={"SignUp"} name={"SignUp"} to={"/signup"}>
                            <button className="px-4 py-2 w-3/4 self-center text-white bg-blue-500 rounded hover:bg-blue-600">
                                Create Account
                            </button>
                        </NavLink>
                    </div>
                </div>
            </div>
        </nav>
    )
}

export default HomePage;