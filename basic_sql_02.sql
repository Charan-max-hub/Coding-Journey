

CREATE TABLE students(

    student_id INT PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL,
    student_branch VARCHAR(20) NOT NULL,
    student_semester INT CHECK (student_semester >= 1 AND student_semester <= 8),
    student_address VARCHAR(100),
    student_marks DECIMAL(5,2)
);





ALTER TABLE students
CHANGE column student_marks student_CGPA DECIMAL(3,2);
ADD column student_email VARCHAR(30);
CHANGE column student_address student_city VARCHAR(30);


INSERT INTO students (student_id,student_name,student_branch,student_semester,student_city,student_CGPA)
VALUES 
        (1,'Rahul','CSE',5,'Mysuru',8.90),
        (2,'Priya','CSE',5,'Mandya',9.00),
        (3,'Karan','CSE',5,'Manglore',8.60),
        (4,'Aniketh','CSE',5,'Shivamogga',8.90),
        (5,'Nagendra','CSE',5,'Shivamogga',9.50),
        (6,'Nithin','ISE',4,'Chamarajanagara',8.00),
        (7,'Sohibe','ISE',4,'Mysuru',9.00),
        (8,'Arjun','ECE',3,'Udupi',8.50),
        (9,'Sneha','ECE',3,'Bengaluru',8.00),
        (10,'Varun','EEE',2,'New Dehli',7.00);

Show all students.

Show students only from CSE branch.

Show distinct branch names.

Show top 3 students with highest marks.

Show students sorted by marks in descending order.

Count how many students are in each branch (GROUP BY branch).

Show only branches that have more than 1 student (HAVING COUNT(*) > 1).

Show students whose marks > 60 and semester > 3 (WHERE + AND).

ALTER table students
MODIFY column student_CGPA DECIMAL(10,5);

UPDATE students
set student_CGPA = student_CGPA + 0.5
WHERE student_branch = 'CSE';


SELECT *
FROM students
WHERE student_semester > 3 AND student_CGPA > 7.5
ORDER BY student_CGPA DESC;
SELECT * FROM students;
