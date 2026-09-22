BASE_STYLE = """
<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background: radial-gradient(circle at 0% 0%, #7f7fd5, #86a8e7 50%, #91eae4);
    min-height: 100vh;
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #2d3748;
  }
  .card {
    background: #ffffff;
    padding: 40px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
    width: 380px;
    max-width: 90%;
  }
  h1 {
    color: #2575fc;
    font-size: 24px;
    margin-top: 0;
    margin-bottom: 20px;
    text-align: center;
  }
  label {
    display: block;
    margin-top: 14px;
    margin-bottom: 4px;
    color: #444;
    font-weight: 600;
    font-size: 14px;
  }
  input[type=text], input[type=password], input[type=email], input[type=file] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-sizing: border-box;
    font-size: 14px;
  }
  input[type=submit], button, .btn {
    display: inline-block;
    margin-top: 20px;
    width: 100%;
    padding: 12px;
    background: #2575fc;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 600;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
    box-sizing: border-box;
  }
  input[type=submit]:hover, button:hover, .btn:hover {
    background: #1a5edb;
  }
  a { color: #2575fc; text-decoration: none; font-size: 14px; }
  a:hover { text-decoration: underline; }
  .info p {
    background: #f4f7ff;
    padding: 10px 14px;
    border-radius: 8px;
    margin: 8px 0;
    color: #333;
  }
  .info p b { color: #2575fc; }
  .footer-link { display: block; text-align: center; margin-top: 18px; }
  .badge {
    display: inline-block;
    background: #e6f4ea;
    color: #1e7e34;
    padding: 4px 10px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 13px;
  }
</style>
"""

REGISTER_FORM = BASE_STYLE + """
<div class="card">
  <h1>Create Your Account</h1>
  <form method="POST" enctype="multipart/form-data">
    <label>Username</label>
    <input type="text" name="username" required>
    <label>Password</label>
    <input type="password" name="password" required>
    <label>First Name</label>
    <input type="text" name="firstname" required>
    <label>Last Name</label>
    <input type="text" name="lastname" required>
    <label>Email</label>
    <input type="email" name="email" required>
    <la
