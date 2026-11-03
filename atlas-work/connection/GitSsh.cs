using System;
using System.IO;
using System.Text;
using System.Diagnostics;
using System.Collections.Generic;
using System.Threading;
class GitSsh {
 static string Quote(string s) {
  var b=new StringBuilder("\"");int n=0;
  foreach(char c in s) {
   if(c=='\\'){n++;continue;}
   if(c=='\"'){b.Append('\\',n*2+1);b.Append(c);n=0;continue;}
   b.Append('\\',n);b.Append(c);n=0;
  }
  b.Append('\\',n*2);b.Append('"');return b.ToString();
 }
 static int Main(string[] args) {
  string dir=AppDomain.CurrentDomain.BaseDirectory;
  var all=new List<string>(new string[]{"-F","none","-i",Path.Combine(dir,"zsery_zsery_deploy_ed25519"),"-o","IdentitiesOnly=yes","-o","BatchMode=yes","-o","StrictHostKeyChecking=yes","-o","UserKnownHostsFile="+Path.Combine(dir,"github_known_hosts"),"-o","HostKeyAlgorithms=ssh-ed25519","-o","ConnectTimeout=20"});
  all.AddRange(args);var quoted=new List<string>();foreach(string s in all)quoted.Add(Quote(s));
  var start=new ProcessStartInfo(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.System),"OpenSSH","ssh.exe"),String.Join(" ",quoted.ToArray()));start.UseShellExecute=false;start.CreateNoWindow=true;
  start.RedirectStandardInput=true;start.RedirectStandardOutput=true;start.RedirectStandardError=true;
  using(var p=Process.Start(start)){
   var input=new Thread(delegate(){try{Console.OpenStandardInput().CopyTo(p.StandardInput.BaseStream);p.StandardInput.Close();}catch{}});input.IsBackground=true;
   var output=new Thread(delegate(){p.StandardOutput.BaseStream.CopyTo(Console.OpenStandardOutput());});
   var error=new Thread(delegate(){p.StandardError.BaseStream.CopyTo(Console.OpenStandardError());});
   input.Start();output.Start();error.Start();p.WaitForExit();output.Join();error.Join();return p.ExitCode;
  }
 }
}
