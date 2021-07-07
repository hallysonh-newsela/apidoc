import { Injectable } from '@nestjs/common';
import { User, UserIn } from './users.model';

@Injectable()
export class UserService {
  private users: User[] = [
    { id: 1, username: "hallyson.almeida", email: "hallysonh@gmail.com", fullName: "Hallyson Almeida", joined: new Date("2021-07-10 12:20:00") },
    { id: 2, username: "mike.jonhson", email: "mike.jonhson.test@gmail.com", fullName: "Mike Jonhson", joined: new Date("2021-03-15 12:30:00") },
    { id: 3, username: "john.rock", email: "john.rock.test@gmail.com", fullName: "John Rock", joined: new Date("2021-07-01 12:40:00") },
  ];

  getList(query: string = null, skip = 0, limit = 100) {
    let result = this.users;
    if (query) {
      result = result.filter(x => x.fullName?.toLowerCase().indexOf(query.toLowerCase()) >= 0);
    }
    return result.slice(skip, skip + limit);
  }

  getById(userId: number) {
    return this.users.find(x => x.id == userId);
  }

  save(userIn: UserIn) {
    delete userIn.password;
    const user = {
      ...userIn,
      id: this.users.length + 1,
      joined: new Date(),
    };
    this.users.push(user);
    return user;
  }

  update(userId: number, userIn: UserIn) {
    const itemIndex = this.users.findIndex(x => x.id == userId);
    if (itemIndex < 0) {
      return null;
    }
    delete userIn.password;
    const user = this.users[itemIndex];
    const updateUser = { ...user, ...userIn };
    this.users[itemIndex] = updateUser;
    return updateUser;
  }
}
