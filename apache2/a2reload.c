#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
   setuid( 0 );
   system( "/etc/init.d/apache2 reload" );

   return 0;
}
