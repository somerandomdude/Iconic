This build requries the ant-contrib library.
Copy the ant-contrib jar to your [ant]/lib folder.
--

If java runs out of memory when compiling add the following to your Environment Variables...

name: ANT_OPTS
value: -Xms512m -Xmx512m