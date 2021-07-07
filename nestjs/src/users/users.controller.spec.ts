import { Test, TestingModule } from '@nestjs/testing';
import { UserController } from './users.controller';
import { UserService } from './users.service';

describe('UserController', () => {
  let app: TestingModule;
  let controller: UserController;

  beforeAll(async () => {
    app = await Test.createTestingModule({
      controllers: [UserController],
      providers: [UserService],
    }).compile();

    controller = app.get<UserController>(UserController);
  });

  describe('getUserList', () => {
    it('should return a list with 3 items', () => {
      expect(controller.getUserList().length).toBe(3);
    });
  });
});
