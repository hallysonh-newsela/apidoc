import { Controller, Get } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { ApiExcludeEndpoint } from '@nestjs/swagger';

@Controller()
export class AppController {
  constructor(private readonly configService: ConfigService) { }

  @Get()
  @ApiExcludeEndpoint()
  getRoot(): string {
    const env = this.configService.get("ENVIRONMENT");
    return `Hello from NestJS App! (ENV: ${env})`;
  }
}
