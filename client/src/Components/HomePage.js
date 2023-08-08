import React from 'react'
import 'tailwindcss/tailwind.css';

function HomePage() {

    return (
        <div className="flex h-screen bg-orange-200">
            {/* Left side */}
            <div className="flex items-center justify-center w-1/2 bg-orange-200">
                <img src="https://ali-practice-aws-bucket.s3.amazonaws.com/Birthdaze_logo-removebg-preview.png" alt="Logo" className="w-[65%]" />
            </div>
    
            {/* Right side */}
            <div className="flex flex-col items-center justify-center w-1/2 bg-orange-200">
                <h1 className="mb-4 text-5xl font-bold text-gray-700">
                    Never forget a birthday again
                </h1>
                <h2 className='mb-4 text-2xl font-bold text-blue-500'>
                    Join Today.
                </h2>
                <button className="px-4 py-2 mb-2 text-white bg-blue-500 rounded hover:bg-blue-600">
                    Sign in
                </button>
                <div className="mb-4 text-2l font-bold text-gray-700">
                    OR
                </div>
                <button className="px-4 py-2 text-white bg-blue-500 rounded hover:bg-blue-600">
                    Create Account
                </button>
            </div>
        </div>
    )
}

export default HomePage;