<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .login-box {
            background: white;
            padding: 40px;
            border-radius: 10px;
            width: 300px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            text-align: center;
        }

        .login-box h2 {
            margin-bottom: 20px;
        }

        .input-box {
            margin-bottom: 15px;
            text-align: left;
        }

        .input-box label {
            font-size: 14px;
        }

        .input-box input {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .login-btn {
            width: 100%;
            padding: 10px;
            background: #4facfe;
            border: none;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }

        .login-btn:hover {
            background: #007bff;
        }

        .extra {
            margin-top: 15px;
            font-size: 13px;
        }

        .extra a {
            text-decoration: none;
            color: #4facfe;
        }
    </style>
</head>

<body>

<div class="login-box">
    <h2>Login</h2>

    <form>
        <div class="input-box">
            <label>Email</label>
            <input type="email" placeholder="Enter email" required>
        </div>

        <div class="input-box">
            <label>Password</label>
            <input type="password" placeholder="Enter password" required>
        </div>

        <button type="submit" class="login-btn">Login</button>
    </form>

    <div class="extra">
        <p>Don't have an account? <a href="#">Sign up</a></p>
    </div>
</div>

</body>
</html>
