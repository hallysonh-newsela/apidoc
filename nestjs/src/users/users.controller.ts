import { Body, Controller, Get, NotFoundException, Param, ParseIntPipe, Post, Put, Query, UsePipes } from '@nestjs/common';
import { ApiCreatedResponse, ApiNotFoundResponse, ApiOkResponse, ApiOperation, ApiTags } from '@nestjs/swagger';
import { JoiValidationPipe } from '../core/joi.validation.pipe';
import { PageQuery, User, UserIn, userInSchema } from './users.model';
import { UserService } from './users.service';

@ApiTags('users')
@Controller('users')
export class UserController {
  constructor(private readonly userService: UserService) { }

  @Get()
  @ApiOkResponse({ type: [User] })
  getUserList(@Query() params?: PageQuery): User[] {
    const { q: query, skip, limit } = params || {};
    return this.userService.getList(query, skip, limit);
  }

  @Get(':userId')
  @ApiOkResponse({ type: User })
  @ApiNotFoundResponse({ description: "User not found" })
  getUserById(@Param('userId', ParseIntPipe) userId: number) {
    const user = this.userService.getById(userId);
    if (!user) {
      throw new NotFoundException(null, "User not found");
    }
    return user;
  }

  @Post()
  @ApiOperation({
    summary: "Create an user",
    description: "Create an user with with the username, email, full_name and password provided",
  })
  @ApiCreatedResponse({ type: User })
  @UsePipes(new JoiValidationPipe(userInSchema))
  createUser(@Body() user: UserIn) {
    return this.userService.save(user);
  }

  @Put(':userId')
  @ApiOkResponse({ type: User })
  @ApiNotFoundResponse({ description: "User not found" })
  @UsePipes(new JoiValidationPipe(userInSchema))
  updateUser(@Param('userId', ParseIntPipe) userId: number, @Body() userIn: UserIn) {
    const user = this.userService.update(+userId, userIn);
    if (!user) {
      throw new NotFoundException(null, "User not found");
    }
    return user;
  }
}
