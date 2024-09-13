import React, { useState } from 'react';

function TeacherDashboard() {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    const handleSubmit = async () => {
        const response = await fetch('/teachers/lessons', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title, content }),
        });
        if (response.ok) {
            alert('Lesson added successfully!');
        }
    };

    return (
        <div>
            <h1>Add New Lesson</h1>
            <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Lesson Title" />
            <textarea value={content} onChange={(e) => setContent(e.target.value)} placeholder="Lesson Content" />
            <button onClick={handleSubmit}>Submit</button>
        </div>
    );
}

export default TeacherDashboard;
