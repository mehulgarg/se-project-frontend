export class Users {
    public name: string;
    public courses: string[] = [];


    constructor(name) {
        this.name = name;
    }

    addCourses(course: string) {
        if (this.courses.indexOf(course) === -1) {
            this.courses.push(course);
        }
    }

    getCourses() {
        return this.courses;
    }
}
