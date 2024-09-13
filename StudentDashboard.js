import React, { useState, useEffect } from 'react';

function StudentDashboard() {
    const [lessons, setLessons] = useState([]);

    useEffect(() => {
        fetch('/students/lessons')
            .then(response => response.json())
            .then(data => setLessons(data));
    }, []);

    return (
        <div>
            <h1>Your Lessons</h1>
            {lessons.map(lesson => (
                <div key={lesson.id}>
                    <h3>{lesson.title}</h3>
                    <p>{lesson.content}</p>
                </div>
            ))}
        </div>
    );
}

export default StudentDashboard;
