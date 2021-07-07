import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';
import * as Joi from 'joi';

// MODEL ////////////////

class UserBase {
  @ApiProperty()
  username: string;
  @ApiProperty()
  email: string;
  @ApiPropertyOptional()
  fullName?: string;
}

export class UserIn extends UserBase {
  @ApiProperty()
  password: string;
}

export class User extends UserBase {
  @ApiProperty()
  id: number;
  @ApiProperty({type: Date})
  joined: Date;
}

export class PageQuery {
  @ApiPropertyOptional()
  q: string;
  @ApiPropertyOptional()
  skip: number = 0;
  @ApiPropertyOptional()
  limit: number = 100;
}

// SCHEMA ////////////////

export const userInSchema = Joi.object({
  username: Joi.string().min(3).max(30).required(),
  email: Joi.string().email({
    minDomainSegments: 2,
    tlds: { allow: ['com', 'net'] },
  }).required(),
  fullName: Joi.string().optional(),
  password: Joi.string().pattern(new RegExp('^[a-zA-Z0-9]{3,30}$')).required(),
})
