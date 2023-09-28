import React from 'react';

function CardBirthday({ birthday }) {
    return (
        <div className="flex flex-col items-center border border-gray-300 p-4 my-4 rounded-lg shadow-md w-[70%]">
            <h3 className="text-xl mb-2">{birthday.name}</h3>
            <p className="text-gray-600">Birthday: {birthday.date}</p>
            <button className=' mt-2'>Edit</button>
        </div>
        
    );
}

export default CardBirthday;