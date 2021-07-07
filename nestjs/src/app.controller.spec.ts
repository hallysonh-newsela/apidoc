import { Test, TestingModule } from '@nestjs/testing';
import { AppController } from './app.controller';
import { ConfigService } from '@nestjs/config';

describe('AppController', () => {
  let app: TestingModule;
  let config: ConfigService;

  beforeAll(async () => {
    app = await Test.createTestingModule({
      controllers: [AppController],
      providers: [ConfigService],
    }).compile();

    config = app.get<ConfigService>(ConfigService);
  });

  describe('getRoot', () => {
    it('should return Hello!', () => {
      const appController = app.get<AppController>(AppController);
      const env = config.get("ENVIRONMENT");
      expect(appController.getRoot()).toBe(`Hello from NestJS App! (ENV: ${env})`);
    });
  });
});
